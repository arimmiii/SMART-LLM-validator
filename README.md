# SMART-LLM 계획 오류 검증과 재생성 실험

[SMART-LLM](https://github.com/SMARTlab-Purdue/SMART-LLM)이 만든 다중 로봇 작업 계획 코드의 오류를 분석하고, 실행 전 자동 검증과 재생성으로 보완한 실험입니다. 원본 프로젝트의 소개는 이 문서 아래쪽에 있습니다.

## 추가한 것

| 파일 | 내용 |
|---|---|
| `scripts/validate_plan.py` | 코드를 실행하지 않고 AST로 검사하는 정적 검증기 (로봇 인자, 로봇 기술, 손 상태, 없는 물건 등) |
| `scripts/regen_loop.py` | 검증 오류를 모델에 알려 최대 3회 다시 생성하는 재생성 루프 |
| `scripts/run_llm.py` | 로봇 이름이 태스크끼리 덮어쓰이는 버그 수정, 할당 단계 토큰 한도를 환경 변수로 설정 |
| `data/aithor_connect/` | 느린 환경에서 동작 대기열이 밀리지 않도록 수정 |
| `results/` | 실험 결과, 진행 기록(`results/sim/progress.md`), 실행 영상(`results/sim/videos/`) |

## 결과

태스크 9개를 토큰 한도 2가지(400, 1500)로 나눠 실험했습니다. gpt-4o-mini와 AI2-THOR를 사용했습니다.

| 기준 | 비교 대상 | 결과 |
|---|---|---|
| 검증기 통과 | 원본 → 보강 규칙으로 재생성 | 18개 중 3개 → 14개 |
| 시뮬레이터 목표 달성(TC) | 기존 규칙 재생성 → 보강 규칙 재생성 | 12개 중 7개 → 11개 |

시뮬레이터 실패는 12개 중 3개에서 0개로, 판정 불가(시간 초과 등)는 2개에서 1개로 줄었습니다.

### 한계

- 실패를 보고 만든 규칙을 같은 태스크에 다시 적용한 결과라서, 처음 보는 태스크에서도 효과가 있는지는 확인하지 않았습니다.
- 조건별로 1~2회만 실행했고, 같은 코드도 실행마다 결과가 달랐습니다.
- TC는 마지막 상태만 확인합니다. 씻기 태스크 3개는 씻었는지를 확인하지 않아, 12개 중 6개가 여기에 해당합니다.
- Slice apple과 Toast a slice는 4번 시도해도 검증을 통과하지 못했고, Slice the tomato(한도 1500)는 30분 안에 끝나지 않았습니다.

## 실행 방법

Python 3.11과 `openai<1.0.0` 환경에서 실행했습니다.

```bash
# 계획 생성: 할당 단계 토큰 한도를 지정
ALLOC_MAX_TOKENS=1500 python3 scripts/run_llm.py --floor-plan 21 --gpt-version gpt-4o-mini

# 정적 검증
python3 scripts/validate_plan.py logs --csv results/validate.csv

# 검증 실패 시 재생성
python3 scripts/regen_loop.py logs/<폴더> --max-retries 3 --suffix _retry2

# 시뮬레이터 실행: GPU가 없으면 화면 크기를 줄임
SIM_SIZE=300 python3 scripts/execute_plan.py --command <폴더>_retry2
```

---

# **SMART-LLM: 대규모 언어 모델을 활용한 다중 에이전트 로봇 작업 계획**

Shyam Sundar Kannan, Vishnunandan L. N. Venkatesh, Byung-Cheol Min.

IEEE International Conference on Robotics and Automation (ICRA) 2024 투고

[프로젝트 페이지](https://sites.google.com/view/smart-llm/) | [arXiv](https://arxiv.org/abs/2309.10062) | [영상](https://www.youtube.com/watch?v=mssTPl7ifyI)

**초록:** 이 연구에서는 실제 환경에서 동작하는 다중 로봇의 작업 계획을 위한 혁신적인 프레임워크인 SMART-LLM을 소개합니다. SMART-LLM(Smart Multi-Agent Robot Task Planning using Large Language Models)은 대규모 언어 모델(LLM)을 활용해, 입력으로 받은 고수준 작업 지시를 다중 로봇 작업 계획으로 변환합니다. 이를 위해 작업 분해, 로봇 팀 구성, 작업 할당의 단계를 차례로 수행하며, 각 단계는 퓨샷(few-shot) 프롬프트 방식의 프로그램 형태 LLM 프롬프트로 진행됩니다. 또한 다중 로봇 작업 계획 문제를 검증하기 위한 벤치마크 데이터셋을 만들었으며, 이 데이터셋은 작업 복잡도가 서로 다른 4가지 범주의 고수준 지시로 구성됩니다. 시뮬레이션과 실제 환경에서 평가 실험을 진행한 결과, 제안한 모델이 다중 로봇 작업 계획 생성에서 유망한 성능을 보였습니다.

## 설치
conda 환경(또는 virtualenv)을 만듭니다.
```
conda create -n smartllm python==3.9
```

의존성을 설치합니다.
```
pip install -r requirments.txt
```

## OpenAI API 키 만들기
이 코드는 OpenAI API를 사용합니다. https://platform.openai.com/ 에서 API 키를 만듭니다.

프로젝트 최상위 폴더에 ```api_key.txt``` 파일을 만들고, 그 안에 OpenAI 키를 붙여 넣습니다.

## 스크립트 실행
아래 명령을 실행하면, 지정한 AI2Thor 평면도에서 작업을 수행하는 파이썬 실행 스크립트가 생성됩니다.

AI2Thor 평면도별 구조는 https://ai2thor.allenai.org/demo 를 참고하세요.
```
python3 scripts/run_llm.py --floor-plan {floor_plan_no}
```
참고: 다른 버전의 GPT 모델로 실행하거나 테스트 데이터셋을 바꾸는 방법은 스크립트를 참고하세요.

위 스크립트는 실행 가능한 코드를 만들어 ```logs``` 폴더에 저장합니다.


아래 스크립트를 실행하면 위에서 생성한 코드를 AI2THOR 환경에서 실행합니다.

실행할 대상을 ```command``` 매개변수로 넘겨야 합니다. ```command```에는 생성된 실행 계획이 저장된 ```logs``` 폴더 안의 폴더 이름을 넣습니다.
```
python3 scripts/execute_plan.py --command {command}
```
## 데이터셋
이 저장소에는 서로 다른 로봇이 함께 수행하는 작업을 위해, 다양한 명령과 여러 기술을 가진 로봇들이 들어 있습니다.

작업의 종류, 작업에 사용할 수 있는 로봇, 평가에 쓰는 작업 후 환경의 최종 상태는 ```data\final_test\```를 참고하세요.

파일 이름은 작업이 실행되는 AI2THOR 평면도에 해당합니다.

최종 테스트에 사용한 로봇 목록과 각 로봇의 기술은 ```resources\robots.py```를 참고하세요.


## 인용
이 연구가 도움이 되었다면 아래와 같이 인용해 주세요.
```
@article{kannan2023smart,
    title={SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models},
  	author={Kannan, Shyam Sundar and Venkatesh, Vishnunandan LN and Min, Byung-Cheol},
  	journal={arXiv preprint arXiv:2309.10062},
 	year={2023}
}
```
