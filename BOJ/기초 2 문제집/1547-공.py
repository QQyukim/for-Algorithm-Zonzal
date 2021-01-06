# 맨 처음 1번 컵 위치 아래에 공 넣고 컵만 바꿈

import sys

m = int(sys.stdin.readline().strip())
cups = [1, 2, 3]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    aIdx = cups.index(a)
    bIdx = cups.index(b)
    cups[aIdx], cups[bIdx] = cups[bIdx], cups[aIdx]

print(cups[0])