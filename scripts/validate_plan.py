#!/usr/bin/env python3
"""
validate_plan.py
SMART-LLM이 logs/ 에 저장한 code_plan.py 를 '실행 전에' 정적으로 검증한다.
(시뮬레이터/API 불필요, 표준 라이브러리만 사용)

검사 항목
  [형식]  format_fence        코드블록(```)이 섞여 있음
          format_extra_text   코드 밖에 설명문이 섞여 있음
          maybe_truncated     출력이 중간에 잘린 것으로 보임(마지막 글자 기준 추정)
  [치명]  no_code / syntax_error
          redefines_robots    모델이 robots 리스트를 코드 안에서 다시 정의함
          unknown_function    정의되지 않은/스킬 목록에 없는 함수 호출
          skill_not_allowed   해당 로봇이 갖지 않은 스킬 사용 (log.txt의 robots 기준)
          unknown_object      환경(objects)에 없는 객체 참조
          double_pickup       이미 물체를 든 로봇이 또 집기
          not_holding         들고 있지 않은 물체를 놓기/던지기 (로봇 간 핸드오프 누락)
          wrong_object        든 물체와 다른 물체를 놓기/던지기
          robot_arg_is_string 로봇 대신 문자열 전달 ('robot1', robots[0]['name'], 그 값을 담은 변수)
          ends_holding        계획이 끝날 때 로봇이 아직 물체를 들고 있음
          receptacle_rejects  시뮬레이터가 받지 않는 물체를 놓기 (자르지 않은 Bread -> Toaster)
  [평가]  goal_static         log.txt 의 ground_truth 와 최종 상태 비교 (True/False/빈칸=판단 불가)
                              정답을 쓰므로 exec_valid 와 재생성 피드백에는 반영하지 않는다

사용법
  python3 scripts/validate_plan.py logs                 # logs 아래 전부
  python3 scripts/validate_plan.py logs/Slice_the_tomato_plans_10-29-2026-12-06-19
  python3 scripts/validate_plan.py logs --csv results/validation.csv
"""
import argparse
import ast
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

KNOWN_SKILLS = {
    'GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject',
    'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', 'DropHandObject',
    'ThrowObject', 'PushObject', 'PullObject',
}
SAFE_CALLS = {'print', 'len', 'range', 'list', 'int', 'str', 'float',
              'enumerate', 'zip', 'min', 'max', 'sum', 'sorted', 'all', 'any'}
FORMAT_ISSUES = {'format_fence', 'format_extra_text', 'maybe_truncated'}
STR_ARG = '<string-arg>'   # 함수 인자로 문자열('robot1')이 들어온 경우의 표식

FENCE = re.compile(r"```(?:python|py)?[ \t]*\n(.*?)```", re.S)


# --------------------------------------------------------------------------
# 1) log.txt 에서 모델명 / 로봇 / 객체 정보 읽기
# --------------------------------------------------------------------------
def read_log_info(folder: Path):
    info = {'model': '?', 'robots': None, 'objects': None, 'ground_truth': None}
    p = folder / 'log.txt'
    if not p.exists():
        return info
    for line in p.read_text(errors='ignore').splitlines():
        if line.startswith('GPT Version:'):
            info['model'] = line.split(':', 1)[1].strip()
        elif line.startswith('robots = '):
            try:
                info['robots'] = ast.literal_eval(line[len('robots = '):])
            except Exception:
                pass
        elif line.startswith('ground_truth = '):
            try:
                info['ground_truth'] = ast.literal_eval(line[len('ground_truth = '):])
            except Exception:
                pass
        elif line.startswith('objects = '):
            try:
                objs = ast.literal_eval(line[len('objects = '):])
                info['objects'] = {o['name'] for o in objs}
            except Exception:
                pass
    return info


# --------------------------------------------------------------------------
# 2) 모델 출력에서 코드만 추출 + 형식 문제 탐지
# --------------------------------------------------------------------------
def extract_code(text: str):
    issues = []
    stripped = text.rstrip()
    # 코드블록이 없고 파이썬으로 온전히 파싱되면 잘린 게 아니다
    complete = False
    if '```' not in text:
        try:
            ast.parse(text)
            complete = True
        except SyntaxError:
            pass
    if not complete and stripped and stripped[-1] not in '.!?`)]}"\'*:;#':
        issues.append('maybe_truncated')

    if '```' in text:
        issues.append('format_fence')
        blocks = FENCE.findall(text)
        if not blocks and text.count('```') % 2 == 1:      # 닫히지 않은 코드블록
            blocks = [text.split('```', 1)[1].split('\n', 1)[-1]]
        outside = FENCE.sub('', text).strip()
        if outside:
            issues.append('format_extra_text')
        return '\n\n'.join(blocks), issues
    return text, issues


# --------------------------------------------------------------------------
# 3) AST 분석: 로봇 인자를 전역 로봇 번호로 풀고, 호출 순서대로 이벤트 생성
# --------------------------------------------------------------------------
def _resolve(node, binding):
    """robot_list[0] / robots[1] / robot(단일 로봇 인자) 를 전역 로봇 인덱스(0부터)로.
    로봇 대신 문자열이면(robots[0]['name'], 'robot1') STR_ARG 를 돌려준다."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return STR_ARG
    if isinstance(node, ast.Name):
        v = binding.get(node.id)
        return v if isinstance(v, int) or v == STR_ARG else None
    if isinstance(node, ast.Subscript):
        sl = node.slice
        if type(sl).__name__ == 'Index':          # py3.8 호환
            sl = sl.value
        if isinstance(sl, ast.Constant) and sl.value == 'name':
            return STR_ARG
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name):
        if isinstance(sl, ast.Constant) and isinstance(sl.value, int):
            name, k = node.value.id, sl.value
            if name == 'robots':
                return k
            lst = binding.get(name)
            if lst and k < len(lst):
                return lst[k]
    return None


def _calls_in(nodes):
    out = []
    for n in nodes:
        for c in ast.walk(n):
            if isinstance(c, ast.Call):
                out.append(c)
    out.sort(key=lambda c: (c.lineno, c.col_offset))
    return out


def build_events(tree, issues):
    funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    events = []          # (robot_idx|None, skill, [str args], lineno)
    state = {'threads': False, 'thread_sets': [], 'join_lines': []}

    def expand(fname, argnodes, ctx, depth):
        if depth > 6:
            return
        fn = funcs[fname]
        params = [a.arg for a in fn.args.args]
        b = {}
        for p, a in zip(params, argnodes):
            if isinstance(a, (ast.List, ast.Tuple)):
                b[p] = [_resolve(e, ctx) for e in a.elts]
            elif isinstance(a, ast.Name) and a.id in ctx:
                b[p] = ctx[a.id]
            elif isinstance(a, ast.Subscript):          # f(robots[0]) : 로봇 1대를 직접 전달
                idx = _resolve(a, ctx)
                if idx is not None:
                    b[p] = idx
            elif isinstance(a, ast.Constant) and isinstance(a.value, str):
                b[p] = STR_ARG                          # f('robot1') : 로봇 객체가 아니라 문자열
        for c in _calls_in(fn.body):
            handle(c, b, depth + 1)

    def handle(call, ctx, depth):
        f = call.func
        # threading.Thread(target=fn, args=([robots[0]],))
        if isinstance(f, ast.Attribute) and f.attr == 'Thread':
            state['threads'] = True
            target, argsnode = None, None
            for kw in call.keywords:
                if kw.arg == 'target' and isinstance(kw.value, ast.Name):
                    target = kw.value.id
                if kw.arg == 'args':
                    argsnode = kw.value
            if target in funcs:
                argl = list(argsnode.elts) if isinstance(argsnode, (ast.Tuple, ast.List)) else []
                start = len(events)
                expand(target, argl, ctx, depth)
                used = {e[0] for e in events[start:] if e[0] is not None}
                state['thread_sets'].append((call.lineno, used))
            return
        if not isinstance(f, ast.Name):
            if isinstance(f, ast.Attribute) and f.attr == 'join':
                state['join_lines'].append(call.lineno)
            return                                  # time.sleep, t.start() 등은 무시
        name = f.id
        if name in funcs:
            expand(name, call.args, ctx, depth)
        elif name in KNOWN_SKILLS:
            # 모든 스킬의 첫 인자는 로봇이다. 문자열이 오거나 비어 있으면 로봇 인자 누락
            if not call.args or (isinstance(call.args[0], ast.Constant)
                                 and isinstance(call.args[0].value, str)):
                issues.append(f'missing_robot_arg:{name}')
                return
            robot = _resolve(call.args[0], ctx)
            if robot == STR_ARG:
                issues.append('robot_arg_is_string')   # 시뮬레이터는 robot['name'] 을 읽으므로 TypeError
                return
            sargs = [a.value for a in call.args[1:]
                     if isinstance(a, ast.Constant) and isinstance(a.value, str)]
            events.append((robot, name, sargs, call.lineno))
        elif name not in SAFE_CALLS:
            issues.append(f'unknown_function:{name}')

    # 최상위의 단순 대입(r = robots[0], team = [robots[0], robots[1]])을 따라간다
    env = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            v = n.value
            if isinstance(v, (ast.List, ast.Tuple)):
                lst = [_resolve(e, env) for e in v.elts]
                if lst and all(x is not None for x in lst):
                    env[n.targets[0].id] = lst
            else:
                r = _resolve(v, env)
                if r is not None:
                    env[n.targets[0].id] = r

    top = [n for n in tree.body if not isinstance(n, ast.FunctionDef)]
    for c in _calls_in(top):
        handle(c, env, 0)

    # 같은 로봇이 동시에 도는 두 스레드 (두 스레드 생성 사이에 join 이 없으면 동시로 본다)
    sets, joins = state['thread_sets'], state['join_lines']
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            (li, si), (lj, sj) = sets[i], sets[j]
            both = si & sj
            if both and not any(li < jl < lj for jl in joins):
                issues.append('concurrent_same_robot:' + ','.join(f'robot{r + 1}' for r in sorted(both)))
    return events, state['threads']


def simulate(events, robots_info, objects, issues):
    """로봇별 '손에 든 물체' 상태를 추적한다. 로봇당 첫 오류만 기록(연쇄 오류 방지)."""
    holding, broken, sliced = {}, set(), set()
    unresolved = False
    for robot, skill, sargs, line in events:
        if robot is None:
            unresolved = True
            continue
        label = f'robot{robot + 1}'

        if robots_info is not None and robot < len(robots_info):
            allowed = set(robots_info[robot].get('skills', KNOWN_SKILLS))
            if skill not in allowed:
                issues.append(f'skill_not_allowed:{skill}@{label}')
        if objects is not None:
            for o in sargs:
                if o not in objects:
                    issues.append(f'unknown_object:{o}')

        if robot in broken:
            continue
        obj = sargs[0] if sargs else None
        if skill == 'SliceObject':
            sliced.add(obj)
        if skill == 'PutObject' and len(sargs) > 1 and sargs[1] == 'Toaster' and obj not in sliced:
            issues.append(f'receptacle_rejects:{obj} must be sliced before Toaster')
        if skill == 'PickupObject':
            if holding.get(robot):
                issues.append(f'double_pickup:{label} holds {holding[robot]}, picks {obj}')
                broken.add(robot)
            else:
                holding[robot] = obj
        elif skill in ('PutObject', 'ThrowObject', 'DropHandObject'):
            h = holding.get(robot)
            if h is None:
                issues.append(f'not_holding:{skill}({obj})@{label}')
                broken.add(robot)
            elif skill != 'DropHandObject' and obj and h != obj:
                issues.append(f'wrong_object:{label} holds {h}, {skill} {obj}')
                broken.add(robot)
            else:
                holding[robot] = None
    for robot, held in sorted(holding.items()):
        if held and robot not in broken:
            issues.append(f'ends_holding:robot{robot + 1} holds {held}')
    if unresolved:
        issues.append('note:unresolved_robot_index')
    used = {r for r, *_ in events if r is not None}
    return used


def goal_static(events, ground_truth):
    """코드 기준 최종 상태를 정답과 비교한다. 평가 전용. True/False, 판단 못 하면 None."""
    if not ground_truth:
        return None
    loc, sliced, cooked, thrown = {}, set(), set(), False
    for _, skill, sargs, _ in events:
        if not sargs:
            continue
        obj = sargs[0]
        if skill == 'PickupObject':
            loc.pop(obj, None)
        elif skill == 'PutObject' and len(sargs) > 1:
            if sargs[1] != 'Toaster' or obj in sliced:
                loc[obj] = sargs[1]
        elif skill == 'ThrowObject':
            loc.pop(obj, None)
            thrown = True
        elif skill == 'SliceObject':
            sliced.add(obj)
        elif skill == 'SwitchOn' and obj == 'Toaster':
            cooked |= {o for o, r in loc.items() if r == 'Toaster'}
    verdict = True
    for g in ground_truth:
        for item in g.get('contains') or []:
            if loc.get(item) != g['name']:
                if thrown:
                    return None             # 던진 물체가 어디 떨어지는지는 코드만으로 모른다
                verdict = False
        state = g.get('state')
        if state == 'SLICED':
            verdict = verdict and g['name'] in sliced
        elif state == 'COOKED':
            verdict = verdict and g['name'] in cooked
        elif state not in (None, 'None'):
            return None
    return verdict


# --------------------------------------------------------------------------
# 4) 폴더 하나 검증
# --------------------------------------------------------------------------
def validate_folder(folder):
    folder = Path(folder)
    info = read_log_info(folder)
    text = (folder / 'code_plan.py').read_text(errors='ignore')
    code, issues = extract_code(text)

    result = {
        'folder': folder.name, 'model': info['model'],
        'n_robots_avail': len(info['robots']) if info['robots'] else '',
        'n_robots_used': 0, 'uses_threads': False, 'n_actions': 0, 'goal_static': '',
    }
    tree = None
    try:
        tree = ast.parse(code)
    except SyntaxError:
        issues.append('syntax_error' if re.search(r'\b(GoTo|Pickup|Put|Throw|Slice)\w*\(|SwitchOn\(', text)
                      else 'no_code')

    if tree is not None:
        for n in ast.walk(tree):
            if isinstance(n, ast.Assign) and any(
                    isinstance(t, ast.Name) and t.id == 'robots' for t in n.targets):
                issues.append('redefines_robots')
                break
        events, threads = build_events(tree, issues)
        used = simulate(events, info['robots'], info['objects'], issues)
        if any(i.startswith('missing_robot_arg') for i in issues):
            # 로봇 인자가 빠진 호출은 상태 추적에서 제외되므로, 거기서 생기는 연쇄 오탐을 뺀다
            issues[:] = [i for i in issues if not i.startswith('double_pickup')]
        goal = goal_static(events, info['ground_truth'])
        result.update(n_robots_used=len(used), uses_threads=threads, n_actions=len(events),
                      goal_static='' if goal is None else goal)
        if not events and not any(i.startswith(('missing_robot_arg', 'robot_arg_is_string'))
                                  for i in issues):
            issues.append('no_code')

    issues[:] = list(dict.fromkeys(issues))        # 중복 제거(순서 유지)
    fatal = [i for i in issues
             if i.split(':')[0] not in FORMAT_ISSUES and not i.startswith('note:')]
    result['exec_valid'] = not fatal
    result['clean_output'] = not any(
        i in FORMAT_ISSUES or i in ('no_code', 'syntax_error') for i in issues)
    result['issues'] = ' | '.join(issues)
    return result


# --------------------------------------------------------------------------
# 5) 여러 폴더 + 요약
# --------------------------------------------------------------------------
def find_folders(paths):
    out = []
    for p in map(Path, paths):
        if (p / 'code_plan.py').exists():
            out.append(p)
        elif p.is_dir():
            out += sorted(d for d in p.iterdir() if (d / 'code_plan.py').exists())
    return out


def summarize(rows):
    by = defaultdict(list)
    for r in rows:
        by[r['model']].append(r)
    lines = [f"{'model':<18}{'n':>4}{'exec_valid':>12}{'clean_output':>14}{'parallel':>10}"]
    for m, rs in sorted(by.items()):
        n = len(rs)
        ev = sum(r['exec_valid'] for r in rs)
        co = sum(r['clean_output'] for r in rs)
        pl = sum(bool(r['uses_threads']) for r in rs)
        lines.append(f'{m:<18}{n:>4}{ev:>8}/{n:<3}{co:>10}/{n:<3}{pl:>7}/{n}')
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('paths', nargs='+', help='logs 폴더 또는 개별 결과 폴더')
    ap.add_argument('--csv', help='결과를 CSV로 저장')
    args = ap.parse_args()

    folders = find_folders(args.paths)
    if not folders:
        sys.exit('code_plan.py 가 들어 있는 폴더를 찾지 못했습니다.')
    rows = [validate_folder(f) for f in folders]

    for r in rows:
        mark = 'OK ' if r['exec_valid'] else 'ERR'
        fmt = 'clean' if r['clean_output'] else 'dirty'
        print(f"[{mark}|{fmt}] {r['model']:<14} {r['folder']}")
        if r['issues']:
            print(f"      {r['issues']}")
    print('\n' + summarize(rows))

    if args.csv:
        Path(args.csv).parent.mkdir(parents=True, exist_ok=True)
        with open(args.csv, 'w', newline='', encoding='utf-8-sig') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f'\nCSV 저장: {args.csv}')


if __name__ == '__main__':
    main()
