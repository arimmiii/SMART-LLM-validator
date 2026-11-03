"""시뮬레이터 결과(16개)와 검증기 판정을 대조한다. API 호출 없음."""
import csv, re, sys
from pathlib import Path
sys.path.insert(0, 'scripts')
from validate_plan import validate_folder
rows = [r for r in csv.DictReader(open('results/alloc_tokens_manifest.csv', encoding='utf-8'))]
want = {('400','6'),('400fix','21'),('1500','6'),('1500fix','21')}
tot = dict(old=0)
tab = {}
print(f"{'task':<24}{'cond':<9}{'sim':<9}{'new_valid':<10}{'goal':<7}issues")
for r in rows:
    if (r['condition'], r['floor_plan']) not in want: continue
    d = r['folder'].strip() + '_retry'
    if not (Path('logs')/d/'code_plan.py').exists(): continue
    v = validate_folder(Path('logs')/d)
    f = Path('results/sim')/(d+'.txt')
    if not f.exists():
        continue
    m = re.findall(r'SR:(\d), TC:(\d)', f.read_text(errors='ignore'))
    txt = f.read_text(errors='ignore')
    if m: sim = 'TC'+m[-1][1]
    elif 'TypeError' in txt: sim = 'crash'
    else: sim = 'unknown'
    fail = sim in ('TC0', 'crash')
    key = ('fail' if fail else 'tc1' if sim=='TC1' else 'unknown', v['exec_valid'])
    tab[key] = tab.get(key, 0) + 1
    fatal = [i for i in v['issues'].split(' | ') if i and not i.startswith(('format_','note:','maybe_'))]
    print(f"{d.split('_plans_')[0][:22]:<24}{r['condition']:<9}{sim:<9}{str(v['exec_valid']):<10}{str(v['goal_static']):<7}{' | '.join(fatal)[:70]}")
print(tab)
