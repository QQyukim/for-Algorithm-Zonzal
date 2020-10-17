import sys

sList = []
sum = int(0)

for i in range(5):
    sList.append(int(sys.stdin.readline()))
    if sList[i] < 40:
        sList[i] = 40

for ele in sList:
    sum += ele

print(sum // 5)

# 64 ms