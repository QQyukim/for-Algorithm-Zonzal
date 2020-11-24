import sys
sys.setrecursionlimit(50000)
# 재귀 호출 스택 수 증가 (기본값: 1000)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    return False

t = int(sys.stdin.readline().strip())
result = []

for _ in range(t):
    cnt = 0

    # m: 열, n: 행, k: 배추 개수
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for col in range(m)] for row in range(n)]

    for _ in range(k):
        # a: 열, b: 행
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            # 열 먼저 돌고 행으로
            if dfs(i, j) == True:
                cnt += 1

    result.append(cnt)

for ele in result:
    print(ele)

# 84 ms