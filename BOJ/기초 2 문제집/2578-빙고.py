import sys

pan = []
chairman = []
calledNumIdx = []
row = [0, 0, 0, 0, 0]
col = [0, 0, 0, 0, 0]
cross = [0, 0]

for _ in range(5):
    pan.append(list(map(int, sys.stdin.readline().split())))

# print(pan)

for _ in range(5):
    chairman.append(list(map(int, sys.stdin.readline().split())))

for i in range(5):
    for j in range(5):
        for pIdx in range(len(pan)):
            if pan[pIdx].count(chairman[i][j]) == 0:
                continue
            else:
                calledNumIdx.append([pIdx, pan[pIdx].index(chairman[i][j])])

# print(calledNumIdx)

# [[2, 2], [0, 4], [4, 2], ...]
for cnt in range(25):
    row[calledNumIdx[cnt][0]] += 1
    col[calledNumIdx[cnt][1]] += 1
    if calledNumIdx[cnt][0] == calledNumIdx[cnt][1]:
        cross[0] += 1
    if calledNumIdx[cnt][0] + calledNumIdx[cnt][1] == 4:
        cross[1] += 1
    
    # 3개 이상이 한꺼번에 생기는 상황이 있음!
    if row.count(5) + col.count(5) + cross.count(5) >= 3:
        print(cnt + 1)
        break