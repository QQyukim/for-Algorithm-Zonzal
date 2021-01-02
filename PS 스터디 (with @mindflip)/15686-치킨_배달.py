# 도시: n x n
# r행 c열 = 위쪽부터 r번째 칸, 왼쪽부터 c번째 칸
# r과 c는 1부터 시작함 -> (1, 1)부터 시작!!!
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
#  -> 집을 기준 ★★★
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합

# 두 칸 (r1, c1)과 (r2, c2) 사이의 거리 = |r1-r2| + |c1-c2|
# 0: 빈 칸, 1: 집, 2: 치킨집

# 도시에 있는 치킨집 중에서 최대 M개를 골라 '남기고'
# 나머지 치킨집을 모두 폐업시키면
# 어떻게 고르면 도시의 치킨 거리가 가장 작게 될 지?

# input: N(2 ≤ N ≤ 50), M(1 ≤ M ≤ 13)

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
graph = []
cList = []
hList = []
distList = []


for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)

# print(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            hList.append((i + 1, j + 1))
        elif graph[i][j] == 2:
            cList.append((i + 1, j + 1))

# print(hList, cList)

for hEle in hList:
    dist = []
    for cEle in cList:
        dist.append(abs(hEle[0] - cEle[0]) + abs(hEle[1] - cEle[1]))
    distList.append(dist)
# print(distList)

# M개를 남길 때,
items = [i for i in range(len(cList))]
comList = list(combinations(items, m))
# print(comList)

# ------------------- min 구하기 (난이도: 상) -------------------
tempList = []
# 예 - (0, 1), (0, 2)의 치킨거리 비교
for comTuple in comList: # comTuple = (0, 1), (0, 2)
    cDistByCombiList = []
    for dist in distList:
        cDistFromH = 1000000    # 초기화
        for idx in comTuple: # idx = 0 or 1 / 0 or 2
        # dist = [2, 6, 7, 6, 5] 내에서 최소 거리 구하기
            cDistFromH = min(cDistFromH, dist[idx])
        cDistByCombiList.append(cDistFromH)
    tempList.append(cDistByCombiList)

print(tempList)

minTemp = 1000000
for temp in tempList:
    minTemp = min(minTemp, sum(temp))

print(minTemp)