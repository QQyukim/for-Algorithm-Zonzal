import sys
from collections import deque

nodeList = []
n = int(sys.stdin.readline().strip())
for _ in range(n - 1):
    nodeList.append(list(map(int, sys.stdin.readline().split())))

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for node in nodeList:
    graph[node[0]].append(node[1])
    graph[node[1]].append(node[0])

# print(graph)

def bfs(v, graph):
    parentNode = [0 for _ in range(n + 1)]
    # 0 ~ 7
    queue = deque([v])
    
    while queue:
        v = queue.popleft()
        visited[v] = True

        for child in graph[v]:
            if visited[child] == False:
                parentNode[child] = v
                visited[child] = True
                queue.append(child)
    
    return parentNode

parentNode = bfs(1, graph)
# len(parentNode) = 8
for i in range(2, len(parentNode)):
    print(parentNode[i])