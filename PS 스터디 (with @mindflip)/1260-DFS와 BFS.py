from collections import deque
import sys

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    
    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')

        # 아직 방문하지 않은 인접 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# for문이 3개나 있어서 시간이 오래 걸리는 듯

n, m, v = map(int, sys.stdin.readline().split())
graph = [ [] for _ in range(n + 1) ]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])
    # graph 원소 순서대로 바꿔주기
    
# print(graph)

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)

# 112 ms -> 조금 더 시간 줄이자