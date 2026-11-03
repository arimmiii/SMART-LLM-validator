#!/usr/bin/env python3
"""
batch_eval.py
run_llm.py 를 N번 반복 실행하고, 그때 새로 생긴 logs/ 폴더만 validate_plan.py 로 검증해 집계한다.

사용법 (프로젝트 루트 = SMART-LLM 폴더에서 실행)
  python3 scripts/batch_eval.py --floor-plan 6 --gpt-version gpt-4o-mini --runs 5 --temperature 0.7

주의
  * run_llm.py 의 LM() 은 temperature=0 이 기본이라 같은 입력이면 결과가 거의 같다.
    실행마다의 편차를 보고 싶으면 --temperature 를 0보다 크게 주고,
    run_llm.py 의 LM() 함수 첫 줄에 아래 한 줄을 추가해야 한다.
        temperature = float(os.environ.get("LLM_TEMP", temperature))
    (--temperature 를 주지 않으면 환경변수를 설정하지 않으므로 기존 동작 그대로)
  * 1회 실행 = 태스크 수 x 3단계 API 호출 + ai2thor 구동. 비용/시간을 보고 --runs 를 정하자.
"""
import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_plan import find_folders, summarize, validate_folder  # noqa: E402

import csv  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--floor-plan', type=int, required=True)
    ap.add_argument('--gpt-version', default='gpt-4o-mini')
    ap.add_argument('--runs', type=int, default=3)
    ap.add_argument('--temperature', type=float, default=None,
                    help='지정하면 LLM_TEMP 환경변수로 전달(위 주의사항 참고)')
    ap.add_argument('--logs', default='logs')
    ap.add_argument('--out', default='results')
    args = ap.parse_args()

    logs = Path(args.logs)
    env = dict(os.environ)
    if args.temperature is not None:
        env['LLM_TEMP'] = str(args.temperature)

    all_rows = []
    for i in range(1, args.runs + 1):
        before = {d.name for d in logs.iterdir()} if logs.exists() else set()
        print(f'\n===== run {i}/{args.runs} ({args.gpt_version}, FloorPlan{args.floor_plan}) =====')
        t0 = time.time()
        proc = subprocess.run(
            [sys.executable, 'scripts/run_llm.py',
             '--floor-plan', str(args.floor_plan),
             '--gpt-version', args.gpt_version],
            env=env)
        if proc.returncode != 0:
            print(f'run {i} 실패(returncode={proc.returncode}). 건너뜁니다.')
            continue
        new = [logs / n for n in sorted({d.name for d in logs.iterdir()} - before)]
        rows = [validate_folder(f) for f in find_folders(new)]
        for r in rows:
            r['run'] = i
        all_rows += rows
        print(f'run {i}: {len(rows)}개 태스크, {time.time() - t0:.0f}초')
        print(summarize(rows))

    if not all_rows:
        sys.exit('검증된 결과가 없습니다.')

    print('\n===== 전체 집계 =====')
    print(summarize(all_rows))

    out = Path(args.out)
    out.mkdir(exist_ok=True)
    path = out / f'batch_{args.gpt_version}_fp{args.floor_plan}_{time.strftime("%m%d_%H%M%S")}.csv'
    with open(path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)
    print(f'\nCSV 저장: {path}')


if __name__ == '__main__':
    main()
