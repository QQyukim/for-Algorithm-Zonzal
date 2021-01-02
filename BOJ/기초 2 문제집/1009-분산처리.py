import sys

n = int(sys.stdin.readline().strip())
remList = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1] ]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    aRem = a % 10
    bRem = b % len(remList[aRem])

    answer = remList[aRem][bRem - 1]
    if answer == 0:
        print(10)
    else:
        print(answer)

# 68 ms
# 시간 초과 주의