import sys
from collections import deque

n = int(sys.stdin.readline().strip())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)  # tree 가 아니라 다 이어주는 graph로 생각!

def bfs(start, end, count):
    queue = deque([[start, end, count]])

    while queue:
        v = queue.popleft()

        start = v[0]
        end = v[1]
        count = v[2]

        if start == end:
            return count
        else:
            if not visited[start]:
                visited[start] = True
                count += 1
                for el in graph[start]:
                    if not visited[el]:
                        queue.append([el, end, count])
    
    return -1

print(bfs(a, b, 0))