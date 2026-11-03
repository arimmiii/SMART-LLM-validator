"""manifest 의 조건별로 잘림 여부 / 검증 통과 / 재생성 후 통과를 표로 출력한다. API 호출 없음."""
import ast
import csv
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, 'scripts')
from validate_plan import validate_folder

CLOSED = '.!?`)]}"\'*:;#'
by = defaultdict(list)
with open('results/alloc_tokens_manifest.csv', encoding='utf-8') as f:
    for r in csv.DictReader(f):
        by[r['condition']].append(r)

for cond, rows in by.items():
    print(f'\n===== condition {cond} (n={len(rows)}) =====')
    n_trunc = n_valid = n_retry = n_retry_valid = n_bad_names = 0
    for r in sorted(rows, key=lambda x: x['folder']):
        d = Path('logs') / r['folder']
        alloc = (d / 'allocated_plan.py').read_text(errors='ignore').rstrip()
        trunc = bool(alloc) and alloc[-1] not in CLOSED
        v = validate_folder(d)
        line = [l for l in (d / 'log.txt').read_text(errors='ignore').splitlines()
                if l.startswith('robots = ')][0]
        names = [x['name'] for x in ast.literal_eval(line[9:])]
        bad = names != [f'robot{i + 1}' for i in range(len(names))]
        rd = d.parent / (d.name + '_retry')
        rv = validate_folder(rd)['exec_valid'] if (rd / 'code_plan.py').exists() else None
        n_trunc += trunc
        n_valid += v['exec_valid']
        n_bad_names += bad
        if rv is not None:
            n_retry += 1
            n_retry_valid += rv
        print(f"{r['folder'].split('_plans_')[0][:38]:<40} chars={len(alloc):>5} trunc={trunc!s:<5} "
              f"names_bad={bad!s:<5} valid={v['exec_valid']!s:<5} retry={rv}")
        if not v['exec_valid']:
            print('    issues:', v['issues'][:170])
    print(f'잘림 추정 {n_trunc}/{len(rows)} | 이름 이상 {n_bad_names}/{len(rows)} | '
          f'검증 통과 {n_valid}/{len(rows)} | 재생성 후 통과 {n_retry_valid}/{n_retry}')
