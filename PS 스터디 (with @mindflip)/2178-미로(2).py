from collections import deque
import sys

# y: 행, x: 열
def bfs(graph, y, x):
    # 큐 생성
    queue = deque([[y, x]])

    # 현재 노드 방문 처리
    graph[y][x] = 1
    # queue 반복문 (큐가 빌 때까지)
    while(queue):
        # queue의 front 값을 가져옴
        v = queue.popleft()
        y = v[0]
        x = v[1]
        
        # front 값 기준 자식 탐색
        for i in range(4):
            # 자식 값이 1이면 queue에 새로운 x,y 넣어주고 그 노드의 값 +1
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= 0 and ny < n and nx >= 0 and nx < m:
                if graph[ny][nx] == 1:
                    # 새로운 노드 값 = 현재 노드 값 + 1
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])
            else:
                continue

# n: 행, m: 열 / y: 행(상하), x: 열(좌우)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
dy = [-1, 1, 0, 0] # 상하
dx = [0, 0, -1, 1] # 좌우

for i in range(n):
    eachRow = sys.stdin.readline().strip()
    row = [int(ele) for ele in eachRow]
    graph[i] = row

# graph[행][열] = graph[n][m]
# bfs(행, 열) = bfs(n, m)
bfs(graph, 0, 0)
print(graph[n - 1][m - 1])

# 116 ms