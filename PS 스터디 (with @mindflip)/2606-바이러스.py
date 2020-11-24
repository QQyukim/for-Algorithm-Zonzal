import sys

def dfs(graph, node, visited):
    global count
    visited[node] = True
    if node != 1:
        count += 1

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i , visited)

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [ [] for _ in range(n + 1) ]
count = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])
    # graph 원소 순서대로 바꿔주기
    
# print(graph)

visited = [False] * (n + 1)
dfs(graph, 1, visited)
print(count)

# 68 ms