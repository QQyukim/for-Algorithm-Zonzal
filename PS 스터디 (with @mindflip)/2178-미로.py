from collections import deque
import sys

# 파라미터: 출발지점, 도착지점, 카운트
# bfs: 출발지점이 계속 바뀜 (형제 좌표로) -> 바뀔 때마다 카운트 증가
# x: 행, y: 열
def bfs(graph, startX, startY, count):
    queue = deque([[startX, startY, count]])

    # 현재 노드 방문 처리
    graph[startX][startY] = 0

    # queue 반복문
    while queue:
        # queue의 front 값을 가져옴
        # -> 조건1: 자식 탐색 / 조건2: 목적지에 도달했는가
        v = queue.popleft()
        x = v[0]
        y = v[1]
        currentCount = v[2]
        if x == n - 1 and y == m - 1: # 목적지 도착?
            print(currentCount) # 카운트 출력
            break   # 방문처리 때문에 써 줄 필요는 없어
        else:
            # x, y => 현재 좌표
            # 현재 포지션을 기준으로 사방 좌표를 구해서
            # 그 좌표가 그래프 안에 있는지 확인하고
            # 그 자식을 큐에 넣고, 카운트 올리기
            upDot = [x - 1, y]
            downDot = [x + 1, y]
            leftDot = [x, y - 1]
            rightDot = [x, y + 1]

            # if leftDot[0] < 0 or rightDot[0] >= m or downDot[1] < 0 or upDot[1] >= n:
            if upDot[0] >= 0 and graph[upDot[0]][upDot[1]] == 1:
                graph[upDot[0]][upDot[1]] = 0
                queue.append([upDot[0], upDot[1], currentCount + 1])
            if downDot[0] < n and graph[downDot[0]][downDot[1]] == 1:
                graph[downDot[0]][downDot[1]] = 0
                queue.append([downDot[0], downDot[1], currentCount + 1])
            if leftDot[1] >= 0 and graph[leftDot[0]][leftDot[1]] == 1:
                graph[leftDot[0]][leftDot[1]] = 0
                queue.append([leftDot[0], leftDot[1], currentCount + 1])
            if rightDot[1] < m and graph[rightDot[0]][rightDot[1]] == 1:
                graph[rightDot[0]][rightDot[1]] = 0
                queue.append([rightDot[0], rightDot[1], currentCount + 1])

# n: 행, m: 열
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(n):
    s = sys.stdin.readline().strip()
    row = [int(c) for c in s]
    graph[i] = row

# graph[행][열]
# bfs(행, 열)
bfs(graph, 0, 0, 1)

# 120 ms