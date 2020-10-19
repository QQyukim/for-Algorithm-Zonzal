import sys

inList = []
triName = ""
sumAngles = int(0)
cnt = int(0)

for i in range(3):
    inList.append(int(sys.stdin.readline()))
    sumAngles += inList[i]

if sumAngles != 180:
    triName = "Error"
else:
    for j in range(len(inList)):
        for k in range(j+1, len(inList)):
            if inList[j] == inList[k]:
                cnt += 1
            else:
                continue
    if cnt == 3:
        triName = "Equilateral"
    elif cnt == 1:
        triName = "Isosceles"
    elif cnt == 0:
        triName = "Scalene"

print(triName)

# 72 ms