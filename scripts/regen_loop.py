#!/usr/bin/env python3
"""
regen_loop.py  -  검증 실패 시 오류 메시지를 모델에 돌려주고 코드를 다시 만들게 하는 루프

동작 (폴더 하나당)
  1) 기존 logs/<폴더>/code_plan.py 를 '1번째 시도'로 사용한다 (API 호출 없음)
  2) validate_plan.py 로 검사한다
  3) 실행 불가(exec_valid=False)면 오류 내용을 설명한 메시지를 모델에 보내 다시 만들게 한다
  4) 통과하거나 --max-retries 에 도달할 때까지 2~3 반복
  5) 결과를 logs/<폴더>_retry/ 에 저장한다 (원본은 건드리지 않음)
       code_plan.py      : 코드블록/설명문을 제거한 최종 코드
       code_plan_raw.txt : 모델이 마지막으로 낸 원문
       attempts.txt      : 시도별 검증 결과
     log.txt 의 GPT Version 에 '+retry' 가 붙으므로, 나중에
       python3 scripts/validate_plan.py logs
     를 돌리면 원본과 retry 결과가 모델별로 나뉘어 집계된다.

사용법 (SMART-LLM 폴더에서)
  python3 scripts/regen_loop.py logs/Throw_the_Spatula_in_the_trash_plans_10-29-2026-12-06-19
  python3 scripts/regen_loop.py logs --only-model gpt-4o-mini --max-retries 3

API 사용량: 첫 시도는 재사용하므로, 이미 통과한 폴더는 호출 0회, 실패한 폴더만 재시도 횟수만큼 호출.
(openai<1.0 의 openai.ChatCompletion 문법, api_key.txt 를 그대로 사용)
"""
import argparse
import csv
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.append('.')

import openai  # noqa: E402

import resources.actions as actions  # noqa: E402
from validate_plan import (extract_code, find_folders,  # noqa: E402
                           read_log_info, validate_folder)

GUIDE = {
    'not_holding': ("A robot can only PutObject/ThrowObject/DropHandObject an object that the SAME robot "
                    "is currently holding, i.e. that it picked up itself with PickupObject earlier. "
                    "A robot cannot use an object that only another robot is holding. If different robots "
                    "must work on the same object, the first robot has to PutObject it on a surface or "
                    "receptacle (for example a CounterTop) and the next robot then goes to it and picks it up "
                    "itself. Each call must use a skill that the calling robot has."),
    'double_pickup': ("A robot can hold only one object at a time. Put the first object down "
                      "(or use another robot) before picking up a second one."),
    'wrong_object': ("A robot can only put/throw the object it is currently holding."),
    'skill_not_allowed': ("Each robot may only use the skills listed for it in its robots entry. "
                          "Re-allocate the subtasks so every call uses a skill that robot has."),
    'missing_robot_arg': ("Every skill call takes the robot as its FIRST argument, "
                          "e.g. PutObject(robot, 'Obj', 'Receptacle'). Never omit the robot."),
    'concurrent_same_robot': ("One robot cannot run two threads at the same time. Parallel threads must "
                              "use different robots (there may be more robots available than you used); "
                              "if only one robot is used, run the steps sequentially."),
    'robot_arg_is_string': ("The robot must be passed as an element of the robots list, e.g. robots[0], "
                            "NOT as a string such as 'robot1' or robots[0]['name']. "
                            "Skill functions read robot['name'] themselves."),
    'ends_holding': ("When the plan finishes, no robot may still be holding an object. Check every "
                     "PickupObject: if the object should stay where it was placed, do not pick it up again; "
                     "otherwise put it down at the place the task asks for."),
    'receptacle_rejects': ("A whole Bread does not fit in the Toaster. A robot with SliceObject must call "
                           "SliceObject on the Bread first; only then put it in the Toaster."),
    'unknown_object': "Only use object names that exist in the objects list.",
    'redefines_robots': ("Do NOT define or reassign the variable `robots`; it already exists. "
                         "Use robots[0], robots[1], ... as given."),
    'unknown_function': "Only call the provided skill functions and functions you define yourself.",
    'syntax_error': "The code must be valid Python.",
    'no_code': "You must output the Python code for the task, not a conversational reply.",
}


def raw_line(folder: Path, key: str):
    for line in (folder / 'log.txt').read_text(errors='ignore').splitlines():
        if line.startswith(key):
            return line[len(key):]
    sys.exit(f'{folder}/log.txt 에서 "{key}" 줄을 찾지 못했습니다.')


def build_prompt(folder: Path):
    """run_llm.py 의 'Allocated Code' 단계 프롬프트를 저장된 결과로부터 똑같이 재구성한다."""
    objects_ai = "\n\nobjects = " + raw_line(folder, 'objects = ')
    robots_txt = raw_line(folder, 'robots = ')
    prompt = "from skills import " + actions.ai2thor_actions
    prompt += "\nimport time"
    prompt += "\nimport threading"
    prompt += objects_ai
    code_prompt = Path('data/pythonic_plans/train_task_allocation_code.py').read_text()
    prompt += "\n\n" + code_prompt + "\n\n"
    plan = (folder / 'decomposed_plan.py').read_text()
    solution = (folder / 'allocated_plan.py').read_text()
    curr = prompt + plan
    curr += "\n# TASK ALLOCATION"
    curr += f"\n\nrobots = {robots_txt}"
    curr += solution
    curr += "\n# CODE Solution  \n"
    return curr


def build_feedback(issues_str: str, info: dict) -> str:
    issues = [i.strip() for i in issues_str.split('|') if i.strip()]
    lines = ["Your code failed automatic validation. Problems found:"]
    seen = set()
    for it in issues:
        key = it.split(':')[0].strip()
        if key.startswith(('format_', 'maybe_', 'note')):
            continue
        lines.append(f"- {it}")
        seen.add(key)
    lines.append("")
    for key in GUIDE:
        if key in seen:
            lines.append(GUIDE[key])
    if info.get('robots'):
        lines.append("\nRobot skills:")
        for r in info['robots']:
            lines.append(f"- {r.get('name')}: {r.get('skills')}")
    lines.append("\nWrite the corrected code. Output ONLY the Python code: no markdown code fences, "
                 "no explanations before or after it.")
    return "\n".join(lines)


def call_llm(model, messages):
    r = openai.ChatCompletion.create(model=model, messages=messages, max_tokens=1400,
                                     temperature=0, frequency_penalty=0.4)
    return r["choices"][0]["message"]["content"].strip()


def run_one(folder: Path, max_retries: int, model_override=None, suffix='_retry'):
    info = read_log_info(folder)
    model = model_override or info['model']
    if 'gpt' not in model:
        print(f'  건너뜀: {model} 은(는) 이 스크립트가 지원하지 않는 모델입니다.')
        return None

    out = folder.parent / (folder.name + suffix)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir()
    for fn in ('decomposed_plan.py', 'allocated_plan.py'):
        shutil.copy(folder / fn, out / fn)
    log = (folder / 'log.txt').read_text(errors='ignore').replace(
        f'GPT Version: {info["model"]}', f'GPT Version: {info["model"]}+{suffix.lstrip("_")}')
    (out / 'log.txt').write_text(log)

    prompt = build_prompt(folder)
    messages = [{"role": "system", "content": "You are a Robot Task Allocation Expert"},
                {"role": "user", "content": prompt}]
    raw = (folder / 'code_plan.py').read_text(errors='ignore')

    history = []
    for n in range(max_retries + 1):
        (out / 'code_plan.py').write_text(raw)
        res = validate_folder(out)
        history.append(res)
        status = 'PASS' if res['exec_valid'] else 'FAIL'
        print(f"  시도 {n + 1}: {status}  {res['issues']}")
        if res['exec_valid'] or n == max_retries:
            break
        messages += [{"role": "assistant", "content": raw},
                     {"role": "user", "content": build_feedback(res['issues'], info)}]
        raw = call_llm(model, messages)

    (out / 'code_plan_raw.txt').write_text(raw)
    code, _ = extract_code(raw)
    (out / 'code_plan.py').write_text(code.strip() + "\n")
    (out / 'attempts.txt').write_text("\n".join(
        f"attempt {i + 1}: exec_valid={h['exec_valid']} issues={h['issues']}"
        for i, h in enumerate(history)))
    return {
        'folder': folder.name, 'model': info['model'],
        'orig_exec_valid': history[0]['exec_valid'],
        'final_exec_valid': history[-1]['exec_valid'],
        'api_calls': len(history) - 1,
        'final_issues': history[-1]['issues'],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('paths', nargs='+')
    ap.add_argument('--max-retries', type=int, default=3)
    ap.add_argument('--only-model', help='예: gpt-4o-mini (log.txt 의 GPT Version 기준)')
    ap.add_argument('--model', help='재생성에 쓸 모델 (기본: 원래 모델)')
    ap.add_argument('--out', default='results')
    ap.add_argument('--suffix', default='_retry',
                    help='결과 폴더 접미사. 같은 이름의 기존 폴더는 지워지므로 재측정 때는 새 이름을 쓴다')
    args = ap.parse_args()

    key = Path('api_key.txt')
    if not key.exists():
        sys.exit('api_key.txt 가 현재 폴더에 없습니다. SMART-LLM 폴더에서 실행하세요.')
    openai.api_key = key.read_text()

    folders = [f for f in find_folders(args.paths) if '_retry' not in f.name]
    rows = []
    for f in folders:
        info = read_log_info(f)
        if args.only_model and info['model'] != args.only_model:
            continue
        print(f'\n[{info["model"]}] {f.name}')
        row = run_one(f, args.max_retries, args.model, args.suffix)
        if row:
            rows.append(row)

    if not rows:
        sys.exit('처리한 폴더가 없습니다.')
    n = len(rows)
    before = sum(r['orig_exec_valid'] for r in rows)
    after = sum(r['final_exec_valid'] for r in rows)
    calls = sum(r['api_calls'] for r in rows)
    print(f'\n===== 요약 =====\n재생성 전 실행 가능: {before}/{n}\n재생성 후 실행 가능: {after}/{n}\n추가 API 호출: {calls}회')

    Path(args.out).mkdir(exist_ok=True)
    path = Path(args.out) / f'regen_{time.strftime("%m%d_%H%M%S")}.csv'
    with open(path, 'w', newline='', encoding='utf-8-sig') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f'CSV 저장: {path}')


if __name__ == '__main__':
    main()
