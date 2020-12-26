import sys
from collections import deque

# 네트워크 개수 return
# 각 컴퓨터: 0 ~ n-1
# i와 j번 컴퓨터가 연결됨 -> computers[i][j] = 1
# computer[i][i]는 항상 1입니다.

# 컴퓨터 수만큼 visited 방문 배열 생성
# 해당 번호의 컴퓨터를 방문했다면 visited의 원소를 1로 바꿔줌
# bfs에서 방문 번호와 연결된 번호를 queue에 넣음
# 연결된 번호가 더 이상 없다면, bfs 함수를 빠져나와 answer를 1 증가
        

def solution(n, computers):
    answer = 0
    visited = [0] * n
    startNode = 0
    # 컴퓨터 탐색 시작 번호

    # 함수를 함수 안에 써주면 인자를 넘겨주지 않아도 됨
    def bfs(startNode):
        queue = deque([startNode])

        while queue:
            # v: 컴퓨터 번호
            startCom = queue.popleft();
            
            if visited[startCom] == 0:
                visited[startCom] = 1
            
            # 해당 컴퓨터 번호와 연결된 컴퓨터 번호 찾기
            for conn in range(len(computers[0])):
                if computers[startCom][conn] == 1 and visited[conn] == 0:
                    queue.append(conn)

    while 0 in visited:
        if visited[startNode] == 0:
            bfs(startNode)
            answer += 1
        startNode += 1
    
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))