import sys
from collections import deque
sys.setrecursionlimit(10**5)

queue = deque()
count = 0
isTrue = True
# 좌 우 상 하 위층 아래층
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
# z, h: 높이, y, n: 행, x, m: 열
graph = []
floor = []
m, n, h = map(int, sys.stdin.readline().split())
for z in range(h):
    for y in range(n):
        floor.append(list(map(int, sys.stdin.readline().split())))
    graph.append(floor)
    floor = []


# print(graph)

def bfs():
    global count

    while queue:
        v = queue.popleft()

        x = v[0]
        y = v[1]
        z = v[2]
        count = v[3]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = 1
                    queue.append([nx, ny, nz, count + 1])

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                queue.append([x, y, z, 0])

bfs()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 0:
                isTrue = False

if isTrue:
    print(count)
else:
    print(-1)