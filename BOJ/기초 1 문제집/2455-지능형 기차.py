import sys

inList = []
pList = []
people = int(0)

for i in range(4):
    inList.append(tuple(map(int, sys.stdin.readline().split())))

    people = people - inList[i][0] + inList[i][1]
    pList.append(people)

pList.sort()
print(pList[3])

# 72 ms