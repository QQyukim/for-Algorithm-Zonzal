import sys
import copy

graph = []

n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxCount = 0

# virusList를 리스트 형식으로 미리 생성하면 시간 단축
virusList = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 2:
            virusList.append([x, y])

# n: 행, m: 열
def buildWalls(wallCnt):
    global graph
    global maxCount
    count = 0

    if wallCnt == 3:
        cGraph = copy.deepcopy(graph)
        
        for el in virusList:
            x = el[0]
            y = el[1]
            dfs(cGraph, x, y)

        for line in cGraph:
            for el in line:
                if el == 0:
                    count += 1
            maxCount = max(count, maxCount)

        return
    else:
        for x in range(n):
            for y in range(m):
                if graph[x][y] == 0:
                    graph[x][y] = 1
                    buildWalls(wallCnt + 1)
                    graph[x][y] = 0

def dfs(cGraph, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and cGraph[nx][ny] == 0:
            cGraph[nx][ny] = 2
            dfs(cGraph, nx, ny)
    
buildWalls(0)
print(maxCount)