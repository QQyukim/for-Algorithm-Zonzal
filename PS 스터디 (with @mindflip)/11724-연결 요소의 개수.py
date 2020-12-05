import sys
sys.setrecursionlimit(10**8)
# from collections import deque

# def bfs(graph, dot, visited):
#     queue = deque([dot])
#     visited[dot] = True
#     while queue:
#         nextDot = queue.popleft()

#         for child in graph[nextDot]:
#             if not visited[child]:
#                 queue.append(child)
#                 visited[child] = True

def dfs(graph, dot):
    visited[dot] = True

    for child in graph[dot]:
        if not visited[child]:
            dfs(graph, child)

# graph = [[]]
count = 0

# n: 정점 개수, m: 간선 개수
n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n + 1)
graph = [ [] for _ in range(n + 1) ]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs, bfs 도는 정점 순서를 알고 싶은 게 아니기 때문에 필요 없음
# for i in range(len(graph)):
#     graph[i] = sorted(graph[i])

# for dot in range(1, n + 1):
#     if not visited[dot]:
#         bfs(graph, dot, visited)
#         count += 1

for dot in range(1, n + 1):
    if not visited[dot]:
        dfs(graph, dot)
        count += 1

print(count)

# bfs, dfs: 1036 ms
# sorted 부분 없으면 908 ms