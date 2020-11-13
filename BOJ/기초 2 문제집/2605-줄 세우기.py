import sys

initList = []
resStr = ''

n = int(sys.stdin.readline().strip())
orderList = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    initList.append(i + 1)

    if orderList[i] == 0:   # 그대로
        continue
    else:
        index = initList[i] - (orderList[i] + 1)
        initList.insert(index, initList[i])
        initList.pop(i + 1)

for ele in initList:
    print(ele, end=' ')

# 72 ms