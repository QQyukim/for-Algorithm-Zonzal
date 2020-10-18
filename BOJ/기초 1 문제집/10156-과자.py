import sys

k, n, m = map(int, sys.stdin.readline().split())
res = (k * n) - m

if res >= 0:
    print(res)
else:
    print(0)

# 72 ms