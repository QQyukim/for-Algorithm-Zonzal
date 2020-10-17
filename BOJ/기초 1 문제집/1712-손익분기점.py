import sys

inList = []
inList = list(map(int, sys.stdin.readline().split()))

a = int(inList[0])
b = int(inList[1])
c = int(inList[2])

if b >= c:
    print(-1)
else:
    n = a // (c - b)
    print(n + 1)

# 68 ms