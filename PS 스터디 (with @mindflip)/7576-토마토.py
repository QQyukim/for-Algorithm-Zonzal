import sys
from collections import deque

def bfs():
    global count
    # queue가 빌 때까지 반복
    while queue:
        # queue의 front 값 꺼내기
        v = queue.popleft()
        y = v[0]
        x = v[1]
        count = v[2]

        # 자식 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= 0 and ny < n and nx >= 0 and nx < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    queue.append([ny, nx, count + 1])

# n: 행, m: 열 / y: 행(상하), x: 열(좌우)
m, n = map(int, sys.stdin.readline().split())
graph = []
dy = [-1, 1, 0, 0]  # 상하
dx = [0, 0, -1, 1]  # 좌우
isTrue = True
queue = deque()
count = 0

# graph 생성
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# queue에 시작점(1) 모두 넣기
for row in range(n):
    for col in range(m):
        if graph[row][col] == 1:
            queue.append([row, col, 0])

bfs()

# 모든 토마토가 익어있다면 (모두 1) => 0
# 토마토가 모두 익지는 못하는 상황이면 (하나라도 0) => -1
for row in range(n):
    for col in range(m):
        if graph[row][col] == 0:
            isTrue = False

if isTrue:
    print(count)
else:
    print(-1)

# 2448 ms