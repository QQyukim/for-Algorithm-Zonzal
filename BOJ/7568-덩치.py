inList = []
subList = []
orderList = []

n = int(input())
for i in range(n):
    subList = list(map(int, input().split()))
    inList.append(tuple(subList))
    orderList.append(1)

for i in range(len(inList)):
    for j in range(len(inList)):
        if i == j:
            continue
        else:
            if inList[i][0] < inList[j][0]:
                if inList[i][1] < inList[j][1]:
                    orderList[i] += 1
                else:
                    continue
            else:
                continue

for ele in orderList:
    print(ele, end=' ')