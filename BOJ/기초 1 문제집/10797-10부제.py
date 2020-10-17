import sys

inList = []
cnt = int(0)

n = int(sys.stdin.readline())

inList = list(map(int, sys.stdin.readline().split()))

for ele in inList:
    if n == ele:
        cnt += 1
    else:
        continue

print(cnt)

# 68 ms