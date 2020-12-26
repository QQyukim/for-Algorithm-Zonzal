import sys
from collections import deque
# 1번 노드에서 가장 멀리 떨어진 노드의 개수
# 가장 멀리 떨어진 노드: '최단경로'로 이동했을 때 간선의 개수가 가장 많은 노드
# n: 노드 개수, vertex: 간선 정보
# 간선: 양방향

# 0번째 원소가 오름차순으로 배열되게

def bfs(v, graph, visited):
    count = 0
    queue = deque([[v, count]])

    while queue:
        node = queue.popleft()
        v = node[0]
        count = node[1]

        if visited[v] == 0:
            count += 1
            visited[v] = count

            for node in graph[v]:
                queue.append([node, count])

def solution(n, edge):
    answer = 0
    visited = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    # edge = sorted(edge, key = lambda x : (x[0], x[1]))
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # print(graph)
    # [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]
    bfs(1, graph, visited)
    
    visited = sorted(visited, reverse=True)
    for cnt in visited:
        if cnt == visited[0]:
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
# return: 3