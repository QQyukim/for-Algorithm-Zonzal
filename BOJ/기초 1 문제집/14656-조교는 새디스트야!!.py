import sys

cnt = int(0)
n = int(sys.stdin.readline().strip())
inList = list(map(int, sys.stdin.readline().split()))

for i in range(len(inList)):
    if (i + 1) != inList[i]:
        cnt += 1

print(cnt)

# 76 ms