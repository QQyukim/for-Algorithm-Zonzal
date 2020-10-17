import sys

fList = []
bList = []
minVal = int(10000)

for _ in range(3):
    fList.append(int(sys.stdin.readline()))

for _ in range(2):
    bList.append(int(sys.stdin.readline()))

for fEle in fList:
    for bEle in bList:
        setVal = fEle + bEle - 50
        if minVal > setVal:
            minVal = setVal
        else:
            continue

print(minVal)

# 76 ms