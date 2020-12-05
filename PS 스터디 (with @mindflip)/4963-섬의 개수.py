import sys
sys.setrecursionlimit(10**5)

# x: h, y: w
def dfs(x, y):
    # 방문
    graph[x][y] = 0

    #    상 하 좌 우  좌상 좌하 우상 우하
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            graph[x][y] = 0
            dfs(nx, ny)

cntList = []

# 1: 땅, 0: 바다
while True:
    w, h = map(int, sys.stdin.readline().split())
    
    if w == 0 and h == 0:
        break
    else:
        graph = []
        count = 0
        for _ in range(h):
            graph.append(list(map(int, sys.stdin.readline().split())))

        for x in range(h):
            for y in range(w):
                if graph[x][y] == 1:
                    dfs(x, y)
                    count += 1
        cntList.append(count)

for cnt in cntList:
    print(cnt)

# 100 ms