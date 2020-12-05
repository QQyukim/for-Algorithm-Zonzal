import sys
from collections import deque
sys.setrecursionlimit(10**5)

def bfs():
    while queue:
        v = queue.popleft()
        
        # x: row, y: col, count: 이동횟수
        x = v[0]
        y = v[1]
        count = v[2]

        if x == destX and y == destY:
            print(count)
            return

        for index in range(8):
            nx = x + dx[index]
            ny = y + dy[index]

            if 0 <= nx < i and 0 <= ny < i and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append([nx, ny, count + 1])

n = int(sys.stdin.readline().strip())
dx = [-1, 1, -2, 2, -1, 1, -2, 2]
dy = [2, 2, 1, 1, -2, -2, -1, -1]

for _ in range(n):
    count = 0
    graph = []
    
    i = int(sys.stdin.readline().strip())
    graph = [ [0 for _ in range(i) ] for _ in range(i)]

    startX, startY = map(int, sys.stdin.readline().split())
    destX, destY = map(int, sys.stdin.readline().split())

    if startX == destX and startY == destY:
        print(0)
    else:
        queue = deque([[startX, startY, count]])
        bfs()

# x, y 좌표가 도착 좌표와 같다는 코드: queue.popleft() 다음에 와야함
# 함수를 빠져나오려면 return 사용하기. break 사용하면 36ms 더 느림
# return 사용하지 않으면 시간 초과 걸림