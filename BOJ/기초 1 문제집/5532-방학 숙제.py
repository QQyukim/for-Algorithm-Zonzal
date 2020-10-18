import sys

inList = []

for _ in range(5):
    inList.append(int(sys.stdin.readline()))

if inList[1] % inList[3] != 0:
    k = (inList[1] // inList[3]) + 1
else:
    k = (inList[1] // inList[3])

if inList[2] % inList[4] != 0:
    m = (inList[2] // inList[4]) + 1
else:
    m = (inList[2] // inList[4])

hwDay = max(k, m)

res = inList[0] - hwDay
print(res)

# 72 ms