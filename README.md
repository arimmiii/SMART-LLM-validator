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
