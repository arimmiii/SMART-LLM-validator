#!/bin/bash
# 사용: run_sim.sh <timeout초> <폴더...>  : 폴더마다 시뮬레이터 실행, 출력을 results/sim/<폴더>.txt 에 저장
cd /mnt/c/Users/LG/26-2_IS/SMART-LLM || exit 1
export PATH=~/project_venv/bin:$PATH
T=$1; shift
mkdir -p results/sim
for d in "$@"; do
  out="results/sim/$d.txt"
  echo "=== $d $(date +%T)"
  timeout "$T" python scripts/execute_plan.py --command "$d" > "$out" 2>&1
  echo "exit=$?"
  pkill -f 'thor-' ; sleep 2
  tail -12 "$out" | cut -c1-220
done
echo DONE
