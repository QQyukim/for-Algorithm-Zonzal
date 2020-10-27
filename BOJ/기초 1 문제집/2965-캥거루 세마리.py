import sys

a, b, c = map(int, sys.stdin.readline().split())
maxCnt = max(b-a, c-b)

print(maxCnt - 1)

# 72 ms