import sys

inList = []
cnt = int(0)

inList = list(map(int, sys.stdin.readline().split()))

for i in range(len(inList)):
    for j in range(i+1, len(inList)):
        if inList[i] == inList[j]:
            cnt += 1
            n = inList[i]

if cnt == 0:
    n = max(inList)
    res = n * 100
elif cnt == 1:
    res = 1000 + (n * 100)
else:
    res = 10000 + (n * 1000)

print(res)

# 68 ms