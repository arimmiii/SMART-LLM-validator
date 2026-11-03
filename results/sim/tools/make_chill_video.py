"""Chill the apple(한도 1500)의 저장된 장면으로 자막 영상과 1차 오류 캡처를 만든다. 실험을 다시 돌리지 않는다."""
import glob
import os
import re
import shutil
import subprocess
import sys

import cv2
from PIL import Image, ImageDraw, ImageFont

S = sys.argv[1]
F = '/mnt/c/Windows/Fonts/'
K = lambda s, b=False: ImageFont.truetype(F + ('malgunbd.ttf' if b else 'malgun.ttf'), s)
M = lambda s: ImageFont.truetype(F + 'consola.ttf', s)
d = 'Chill_the_apple_and_wash_the_knife_plans_11-02-2026-14-55-52'
OUT = 'results/sim/videos/'

# ---------- 1차 오류 캡처: 스레드 2개의 출력이 섞여 있어 chill_apple 쪽 줄만 고른다
L = open(f'results/sim/{d}_retry.txt', errors='ignore').read().splitlines()
pick = [L[i - 1] for i in (4, 5, 7, 9, 11, 14, 15, 17, 19, 20, 21)]
pick = [re.sub(r'"/mnt/c/.*?/(executable_plan\.py)"', r'"\1"', x) for x in pick]
print('\n'.join(pick))
assert 'chill_apple' in pick[5] and "'Apple'" in pick[6], 'traceback lines mismatched'
sr = [x for x in L if x.startswith('SR:')][-1]
c1 = [x for x in open(f'logs/{d}_retry/code_plan.py') if 'task1_thread = ' in x][0].strip()
c2 = [x for x in open(f'logs/{d}_retry2/code_plan.py') if 'task1_thread = ' in x][0].strip()
print(c1, c2, sr, sep='\n')
RED, GREEN, WHITE = (255, 110, 110), (120, 230, 140), (255, 255, 255)
rows = [('k', '1차 재생성 실행 로그: Chill the apple and wash the knife (토큰 한도 1500)', WHITE)]
rows += [('m', x, RED if x.startswith('TypeError') else (220, 220, 220)) for x in pick]
rows += [('s', '', 0), ('m', sr, (255, 210, 90)), ('s', '', 0),
         ('k', '원인: 1차 코드는 로봇 정보 대신 이름 글자만 넘김', WHITE), ('m', c1, RED), ('s', '', 0),
         ('k', '2차 재생성에서 고쳐진 코드', WHITE), ('m', c2, GREEN)]
H = 40 + sum({'k': 46, 'm': 32, 's': 16}[r[0]] for r in rows)
im = Image.new('RGB', (1500, H), (24, 24, 28))
D = ImageDraw.Draw(im)
y = 20
for t, s, c in rows:
    if t == 'k':
        D.text((28, y + 4), s, font=K(26, True), fill=c)
        y += 46
    elif t == 'm':
        D.text((28, y), s, font=M(23), fill=c)
        y += 32
    else:
        y += 16
im.save(OUT + 'error_chill_1500_retry.png')

# ---------- 자막 영상: 자막 구간은 장면을 눈으로 확인해 정했다
n = f'logs/{d}_retry2'
views = [('top_view', '위에서 본 화면'), ('agent_1', '로봇 1 시점'), ('agent_2', '로봇 2 시점')]
fl = {v: sorted(glob.glob(f'{n}/{v}/*.png')) for v, _ in views}
N = 61
R1 = [(0, 23, '사과가 있는 곳으로 이동'), (24, 53, '사과를 들고 냉장고로 이동'), (54, 55, '냉장고 문 열기'),
      (56, 57, '사과를 냉장고에 넣기'), (58, 60, '문 닫기, 끝')]
R2 = [(0, 2, '칼이 있는 곳으로 이동'), (3, 35, '칼을 들고 싱크대로 이동'), (36, 38, '칼을 싱크대에 놓기'),
      (39, 45, '물을 틀어 칼 씻기'), (46, 48, '칼을 다시 집기'), (49, 60, '칼을 조리대에 놓고 끝')]
cap = lambda T, i: [t for a, b, t in T if a <= i <= b][0]
VW, TOP, BOT = 480, 64, 96
W, H = VW * 3, TOP + VW + BOT


def card(lines):
    im = Image.new('RGB', (W, H), (20, 20, 24))
    D = ImageDraw.Draw(im)
    y = H // 2 - len(lines) * 34
    for s, sz, b, c in lines:
        f = K(sz, b)
        D.text(((W - D.textlength(s, font=f)) / 2, y), s, font=f, fill=c)
        y += sz + 30
    return im


def frame(i):
    im = Image.new('RGB', (W, H), (20, 20, 24))
    D = ImageDraw.Draw(im)
    D.text((16, 14), '로봇 2대가 동시에 일합니다: 로봇 1은 사과 넣기, 로봇 2는 칼 씻기', font=K(26, True), fill=WHITE)
    for k, (v, l) in enumerate(views):
        a = cv2.cvtColor(cv2.imread(fl[v][i]), cv2.COLOR_BGR2RGB)
        im.paste(Image.fromarray(a).resize((VW, VW), Image.BICUBIC), (k * VW, TOP))
        D.rectangle((k * VW, TOP, k * VW + 190, TOP + 38), fill=(0, 0, 0))
        D.text((k * VW + 10, TOP + 3), l, font=K(22, True), fill=WHITE)
    for k, (name, T) in enumerate((('로봇 1', R1), ('로봇 2', R2)), start=1):
        D.text((k * VW + 14, TOP + VW + 14), name, font=K(20), fill=(150, 200, 255))
        D.text((k * VW + 14, TOP + VW + 44), cap(T, i), font=K(27, True), fill=(255, 230, 120))
    D.text((14, TOP + VW + 44), f'진행 {i + 1}/{N}', font=K(22), fill=(190, 190, 190))
    return im


FPS = 10
hold = {i: 3 for i in range(N)}  # 기본 0.3초, 중요한 동작은 더 오래 보여 준다
for i in (3, 24, 39, 54, 55, 56, 57, 58):
    hold[i] = 12
for i in (36, 37, 38, 46, 47, 48, 49, 50):
    hold[i] = 8
hold[60] = 25
tmp = S + '/vid2'
shutil.rmtree(tmp, ignore_errors=True)
os.makedirs(tmp)
k = 0


def emit(im, count):
    global k
    for _ in range(count):
        im.save(f'{tmp}/{k:05d}.png', compress_level=1)
        k += 1


emit(card([('할 일: "사과를 차갑게 하고 칼을 씻어라"', 44, True, WHITE),
           ('보강한 검증기로 재생성한 코드를 시뮬레이터에서 실행한 화면 (토큰 한도 1500)', 26, False, (210, 210, 210)),
           ('실제 실행은 더 오래 걸렸고, 보기 쉽게 장면별 속도를 조절했습니다', 24, False, (170, 170, 170))]), 40)
for i in range(N):
    emit(frame(i), hold[i])
emit(card([('결과: SR 1, TC 1', 46, True, GREEN),
           ('점수 조건은 "냉장고 안에 사과가 있다"입니다', 28, False, (230, 230, 230)),
           ('칼을 씻었는지는 점수에 들어가지 않습니다', 28, False, (230, 230, 230))]), 40)
print('images', k, 'sec', k / FPS)
frame(39).save(S + '/c39.png')
frame(56).save(S + '/c56.png')
subprocess.check_call(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{tmp}/%05d.png',
                       '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-r', '25',
                       OUT + 'chill_apple_1500_retry2_captioned.mp4'])
