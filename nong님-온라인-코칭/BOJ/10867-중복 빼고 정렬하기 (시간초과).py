# 시간초과

inList = []
outList = []

num = int(input())
inList = list(map(int, input().split()))

for i in range(num):
    tmp = inList[i]
    
    for inEle in inList:
        if tmp == inEle:
            if inEle not in outList:
                outList.append(tmp)
                break
        else:
            continue

outList.sort()
print(outList)