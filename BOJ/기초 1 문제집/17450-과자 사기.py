import sys

snuList = []
maxGaseongbi = 0

for _ in range(3):
    snuList.append(list(map(int, sys.stdin.readline().split())))

# [0]: 가격, [1]: 무게
for i in range(len(snuList)):
    if snuList[i][0] >= 500:
        gaseongbi = (snuList[i][1] * 10) / ((snuList[i][0] * 10) - 500)
    else:
        gaseongbi = snuList[i][1] / snuList[i][0]
    
    if gaseongbi > maxGaseongbi:
        maxGaseongbi = gaseongbi
        ansIndex = i

if ansIndex == 0:
    print("S")
elif ansIndex == 1:
    print("N")
elif ansIndex == 2:
    print("U")

# 72 ms