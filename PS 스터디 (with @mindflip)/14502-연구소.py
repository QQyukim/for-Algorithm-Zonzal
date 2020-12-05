# 시간 초과
import sys
from collections import deque
sys.setrecursionlimit(10**5)

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxCount = 0

# 상하좌우
# (*) 벽은 3개 세움
# 0: 빈 칸, 1: 벽, 2: 바이러스 있는 곳
# 안전 영역 크기 최댓값 = 바이러스 퍼지는 곳 최솟값

# 벽 세우는 로직: 재귀 카운팅 3개
# ** 재귀 함수: 브루트포스 - 모든 경우 다 따짐

# n: 행, m: 열
def buildWalls(wallCnt):
    # count != 3 이면 벽 세우는 작업 계속
    global graph

    if wallCnt == 3:
        # print(graph)
        bfs()
        return
    else:
        for x in range(n):
            for y in range(m):
                if graph[x][y] == 0:
                    graph[x][y] = 1
                    buildWalls(wallCnt + 1)
                    # 재귀 함수 끝남
                    graph[x][y] = 0 # 벽 허물기

# wallCNt = 3일 때 bfs() 실행
# bfs()로 최소 카운트 수집
# 벽 세운 거를 다시 0으로 바꾸는 작업 => 다음 경우의 수
def bfs():
    global maxCount
    count = 0
    queue = deque()

    cGraph = [[0 for _ in range(m) ] for _ in range(n) ]
    for x in range(n):
        for y in range(m):
            cGraph[x][y] = graph[x][y]

    for x in range(n):
        for y in range(m):
            if cGraph[x][y] == 2:
                queue.append([x, y])

    while queue:
        v = queue.popleft()

        x = v[0]
        y = v[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and cGraph[nx][ny] == 0:
                cGraph[nx][ny] = 2
                queue.append([nx, ny])
    
    for line in cGraph:
        for el in line:
            if el == 0:
                count += 1

    maxCount = max(count, maxCount)

n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

buildWalls(0)
print(maxCount)