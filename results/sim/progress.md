# 시뮬레이터 배치 진행 기록

시간 초과는 실패로 세지 않고 판정 불가로 구분한다.

## 2026-11-02 16:21
- 끝난 개수: 16개 중 8개 (한도 400 그룹 완료)
- 한도 400 결과: 목표 달성(TC 1) 3개 (Put mug, Throw the Spatula, Chill the apple), 실패 3개 (Wash the lettuce, Slice the tomato, Toast a slice), 판정 불가(시간 초과) 2개 (Put two vegetables, Wash the fork)
- SR 1: 2개 (Put mug, Throw the Spatula)
- 현재 실행 중: Slice the tomato (한도 1500)

## 2026-11-02 16:42
- 끝난 개수: 16개 중 13개
- 새로 끝난 태스크 (한도 1500): Throw the Spatula SR 1/TC 1, Put mug SR 1/TC 1, Wash the lettuce SR 0/TC 1 (RU 0), Chill the apple SR 0/TC 0 (TypeError), Slice the tomato 판정 불가 (X11 연결 끊김, 점수 없음)
- 현재 실행 중: Put two vegetables (한도 1500)
- 누적 13개: 목표 달성(TC 1) 6개, 그중 SR 1은 4개 / 실패 4개 / 판정 불가 3개 (시간 초과 2, X11 끊김 1)

## 2026-11-02 17:12
- 끝난 개수: 16개 중 15개
- 새로 끝난 태스크 (한도 1500): Put two vegetables 판정 불가 (시간 초과), Toast a slice SR 0/TC 0 (Exec 0.75)
- 현재 실행 중: Wash the fork (한도 1500), 864초 경과 (제한 900초)
- 누적 15개: 목표 달성(TC 1) 6개, 그중 SR 1은 4개 / 실패 5개 / 판정 불가 4개 (시간 초과 3, X11 끊김 1)

## 2026-11-02 17:12 배치 완료
- SIM_SIZE=300, 태스크당 제한 900초, 조건별 1회 실행. 대상은 재생성 후 검증기를 통과한 코드.

| 태스크 | 한도 400 | 한도 1500 |
|---|---|---|
| Put mug | SR 1 / TC 1 | SR 1 / TC 1 |
| Throw the Spatula | SR 1 / TC 1 | SR 1 / TC 1 |
| Chill the apple | SR 0 / TC 1 (RU 0) | 실패: TypeError |
| Wash the lettuce | SR 0 / TC 0 | SR 0 / TC 1 (RU 0) |
| Slice the tomato | 실패: TypeError | 판정 불가: X11 끊김 |
| Toast a slice | SR 0 / TC 0 | SR 0 / TC 0 |
| Put two vegetables | 판정 불가: 시간 초과 | 판정 불가: 시간 초과 |
| Wash the fork | 판정 불가: 시간 초과 | 판정 불가: 시간 초과 |

- 합계 16개: TC 1 6개 (그중 SR 1 4개) / 실패 5개 / 판정 불가 5개 (시간 초과 4, X11 끊김 1)
- 조건별 TC 1: 한도 400 8개 중 3개, 한도 1500 8개 중 3개

## 재실행 결과 (2026-11-02 17:23 시작, 진행 출력 즉시 저장)
- Wash the fork (한도 400, 제한 10분): SR 1 / TC 1
- Wash the fork (한도 1500, 제한 10분): 판정 불가, 시간 초과
- Slice the tomato (한도 1500, 제한 15분): 판정 불가, 시간 초과
- Put two vegetables (한도 400, 제한 40분): 판정 불가, 시간 초과
- Put two vegetables (한도 1500, 제한 40분): 판정 불가, 시간 초과

## 재실행 반영 최종 (2026-11-02 19:16)
| 태스크 | 한도 400 | 한도 1500 |
|---|---|---|
| Put mug | SR 1 / TC 1 | SR 1 / TC 1 |
| Throw the Spatula | SR 1 / TC 1 | SR 1 / TC 1 |
| Wash the fork | SR 1 / TC 1 (재실행) | 판정 불가: 시간 초과 2회 |
| Chill the apple | SR 0 / TC 1 (RU 0) | 실패: TypeError |
| Wash the lettuce | SR 0 / TC 0 | SR 0 / TC 1 (RU 0) |
| Slice the tomato | 실패: TypeError | 판정 불가: X11 끊김 1회, 시간 초과 1회 |
| Toast a slice | SR 0 / TC 0 | SR 0 / TC 0 |
| Put two vegetables | 판정 불가: 시간 초과 2회 | 판정 불가: 시간 초과 2회 |

- 합계 16개: TC 1 7개 (그중 SR 1 5개) / 실패 5개 / 판정 불가 4개
- 조건별 TC 1: 한도 400 8개 중 4개, 한도 1500 8개 중 3개

## 2026-11-02 20:11:58 새 검증기 코드 시뮬레이터 실행 일시 중단
- 사용자 이동으로 중단. 중단 시 실행 중이던 태스크: Slice_the_tomato_plans_11-02-2026-14-33-44_retry2

## 2026-11-02 21:33:15 재개
- 남은 6개(한도 1500) 실행 시작. Slice the tomato 부터 다시 돌림.

## 2026-11-02 22:34 새 코드(_retry2) 배치 완료, 이전 코드와 비교
- SIM_SIZE=300, 태스크당 제한 900초, 조건별 1회 실행. 시간 초과는 판정 불가.
- 이전 코드 Slice/Fork/Lettuce 칸은 재실행 반영 최종 표 기준. 같은 6개 태스크 x 조건 2개 = 12개만 비교.

| 태스크 | 400 이전 | 400 새 코드 | 1500 이전 | 1500 새 코드 |
|---|---|---|---|---|
| Put mug | SR 1 / TC 1 | SR 1 / TC 1 | SR 1 / TC 1 | SR 1 / TC 1 |
| Throw the Spatula | SR 1 / TC 1 | SR 1 / TC 1 | SR 1 / TC 1 | SR 0 / TC 1 (RU 0) |
| Chill the apple | SR 0 / TC 1 (RU 0) | SR 0 / TC 1 (RU 0) | 실패: TypeError | SR 1 / TC 1 |
| Wash the fork | SR 1 / TC 1 | SR 1 / TC 1 | 판정 불가 | 판정 불가 |
| Wash the lettuce | SR 0 / TC 0 | SR 1 / TC 1 | SR 0 / TC 1 (RU 0) | 판정 불가 |
| Slice the tomato | 실패: TypeError | 판정 불가 | 판정 불가 | 판정 불가 |

- 12개 중 이전 코드: TC 1 7개 (SR 1 5개) / 실패 3개 / 판정 불가 2개
- 12개 중 새 코드: TC 1 8개 (SR 1 6개) / 실패 0개 / 판정 불가 4개
- 판정 불가를 범위로 보면 TC 1 이전 7~9개, 새 코드 8~12개로 겹침.
- 시뮬레이터 실행에서 제외된 태스크: Slice apple, Toast (새 검증기 통과 못 함), Put two vegetables (통과했지만 goal_static 불일치). 조건 2개 합쳐 6개.

## 2026-11-03 09:0x 판정 불가 4개 재실행 시작
- 제한 1800초, SIM_SIZE=300. 이전 출력은 *.run1.txt, 이전 화면은 frames_timeout_run1/ 에 보관.
- 이전 실행 화면 확인: Wash the fork(1500)는 마지막 51장이 동일(약 2.7분, 로봇 2대가 붙어 있음). 나머지 3개는 끝까지 화면이 바뀜. 프레임당 4.7~5.6초.

## 2026-11-03 09:33 재실행 중간
- 끝난 개수: 4개 중 2개. 소요: Wash the fork(1500) 9분 51초, Wash the lettuce(1500) 8분 38초.

- Slice the tomato(1500) 재실행: 30분 시간 초과, 판정 불가.

## 2026-11-03 10:03 재실행 완료 (제한 30분, 새 코드)
| 태스크 | 조건 | 이번 결과 | 소요 | 장면 수 |
|---|---|---|---|---|
| Wash the fork | 1500 | SR 0 / TC 1 (RU 0) | 9분 51초 | 110 |
| Wash the lettuce | 1500 | SR 0 / TC 1 (RU 0, Exec 0.67) | 8분 38초 | 90 |
| Slice the tomato | 1500 | 판정 불가: 시간 초과 | 30분 3초 | 321 |
| Slice the tomato | 400 | SR 0 / TC 1 (RU 0) | 약 12분 | 119 |

- 재실행 반영 12개 중 이전 코드: TC 1 7개 (SR 1 5개) / 실패 3개 / 판정 불가 2개
- 재실행 반영 12개 중 새 코드: TC 1 11개 (SR 1 6개) / 실패 0개 / 판정 불가 1개
- 판정 불가를 범위로 보면 TC 1 이전 7~9개, 새 코드 11~12개. 18개 기준 이전 7개, 새 코드 11개.
- 조건별 사실상 1~2회 실행이고 규칙은 같은 태스크의 실패에서 만들었으므로 표본 내 결과.

## 2026-11-03 발표 자료
- 영상: results/sim/videos/chill_apple_1500_retry2_captioned.mp4 (저장된 장면으로 제작, 재실행 없음). 자막 구간은 장면을 눈으로 확인해 정함.
- 1차 오류 캡처: results/sim/videos/error_chill_1500_retry.png

## 2026-11-03 발표 슬라이드
- results/presentation/smart_llm_talk.html (10장, assets 폴더와 함께 옮길 것). N 키: 발표자 대본.

- PDF: results/presentation/smart_llm_talk.pdf (10쪽, 6쪽은 영상의 한 장면).

## 2026-11-03 폴더 정리
- 커밋 후 장면 이미지 삭제(Chill the apple 14-55-52_retry2 제외). frames_timeout_run1, run1_contact 삭제.
