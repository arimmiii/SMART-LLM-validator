#!/usr/bin/env python3
"""
fix_data.py - data/final_test/*.json 의 깨진 줄을 고친다.

문제: 많은 줄에 파이썬식 None (따옴표 없음)이 들어 있어 json.loads 가 읽지 못한다.
      (FloorPlan6 처럼 읽히는 줄은 "None" 문자열을 쓰므로, 같은 형태로 맞춘다)
처리:
  1) 맨 처음 실행 때 data/final_test_backup/ 에 원본을 통째로 백업한다.
  2) 이후에는 항상 백업본을 기준으로 고쳐서 data/final_test/ 에 쓴다 (여러 번 실행해도 안전).
  3) 그래도 읽히지 않는 줄은 data/final_test/ 에서 빼고 목록으로 알려준다 (백업에는 남아 있음).
원복: data/final_test_backup 안의 파일을 data/final_test 로 다시 복사하면 된다.

사용법 (SMART-LLM 폴더에서)
  python3 scripts/fix_data.py
"""
import json
import re
import shutil
from pathlib import Path

src = Path('data/final_test')
bak = Path('data/final_test_backup')
if not src.is_dir():
    raise SystemExit('data/final_test 폴더가 없습니다. SMART-LLM 폴더에서 실행하세요.')
if not bak.exists():
    shutil.copytree(src, bak)
    print(f'원본 백업: {bak}')

# 값 자리(": None," / ": None}" / "[None]")에 있는 것만 바꾼다. 문장 속 단어는 건드리지 않는다.
PATTERNS = [
    (re.compile(r'([:\[,]\s*)None(\s*[,}\]])'), r'\1"None"\2'),
    (re.compile(r'([:\[,]\s*)True(\s*[,}\]])'), r'\1true\2'),
    (re.compile(r'([:\[,]\s*)False(\s*[,}\]])'), r'\1false\2'),
]

def ensure_trans(line):
    """trans / max_trans 가 없으면 임시값 0 을 채운다. 반환: (줄, 채웠는지)"""
    d = json.loads(line)
    if 'trans' in d and 'max_trans' in d:
        return line, False
    new = {k: v for k, v in d.items() if k not in ('trans', 'max_trans')}
    new['trans'] = d.get('trans', 0)
    new['max_trans'] = d.get('max_trans', 0)
    return json.dumps(new, ensure_ascii=False), True


total_fixed = total_dropped = total_filled = 0
for b in sorted(bak.glob('FloorPlan*.json')):
    out, fixed, dropped, filled = [], 0, [], []
    for n, line in enumerate(b.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        try:
            json.loads(line)
        except ValueError:
            cand = line
            for pat, rep in PATTERNS:
                cand = pat.sub(rep, cand)
            try:
                json.loads(cand)
                line = cand
                fixed += 1
            except ValueError as e:
                task = re.search(r'"task"\s*:\s*"([^"]*)"', line)
                dropped.append((n, task.group(1) if task else line[:60], str(e)))
                continue
        line, was_filled = ensure_trans(line)
        if was_filled:
            filled.append((n, json.loads(line)['task']))
        out.append(line)
    (src / b.name).write_text('\n'.join(out) + '\n', encoding='utf-8')
    total_fixed += fixed
    total_dropped += len(dropped)
    total_filled += len(filled)
    print(f'{b.name:<20} 줄 {len(out)}개 사용 (고침 {fixed}, 제외 {len(dropped)}, 임시값 {len(filled)})')
    for n, t, e in dropped:
        print(f'    제외: 줄 {n} "{t}"  ({e})')
    for n, t in filled:
        print(f'    임시값(trans=0, max_trans=0): 줄 {n} "{t}"')

print(f'\n총 {total_fixed}줄 고침, {total_dropped}줄 제외, {total_filled}줄 trans 임시값')
if total_filled:
    print('주의: 임시값 줄은 코드 생성에는 영향이 없지만, trans 기반 채점에는 쓰지 마세요.')
