import sys

stdStr1 = ''
stdStr2 = ''
shapeList = []
resList = []

n = int(sys.stdin.readline().strip())
stdStr1 = sys.stdin.readline().strip().replace(' ', '')

m = int(sys.stdin.readline().strip())
for _ in range(m):
    shapeList.append(sys.stdin.readline().strip().replace(' ', ''))

# # 구현
for direction in stdStr1:
    if direction == '1':
        direction = '3'
    elif direction == '2':
        direction = '4'
    elif direction == '3':
        direction = '1'
    elif direction == '4':
        direction = '2'
    stdStr2 += direction

stdStr2 = stdStr2[::-1]

seqStdStr1 = stdStr1 * 2
seqStdStr2 = stdStr2 * 2

for shapeStr in shapeList:
    if (shapeStr in seqStdStr1) or (shapeStr in seqStdStr2):
        resList.append(shapeStr)

print(len(resList))
for resStr in resList:
    for eachStr in resStr:
        print(int(eachStr), end=' ')
    print()

# 68 ms