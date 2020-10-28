import sys

inList = []
xCnt = int(0)
yCnt = int(0)

for _ in range(3):
    inList.append(tuple(map(int, sys.stdin.readline().split())))

for dot1 in inList:
    xCnt = int(0)
    yCnt = int(0)

    for dot2 in inList:
        if dot1 == dot2:
            continue
        else:
            if dot1[0] != dot2[0]:
                xCnt += 1
                if xCnt == 2:
                    xRes = dot1[0]
            if dot1[1] != dot2[1]:
                yCnt += 1
                if yCnt == 2:
                    yRes = dot1[1]

print(xRes, yRes)

# 68 ms