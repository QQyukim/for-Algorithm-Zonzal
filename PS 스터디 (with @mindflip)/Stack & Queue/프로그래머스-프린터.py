import sys
from collections import deque

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

def solution(priorities, location):
    index = [ i for i in range(len(priorities)) ]
    order = []
    indexOrder = []

    queue = deque(priorities)
    iQueue = deque(index)

    while queue:
        v = queue.popleft()
        iv = iQueue.popleft()
        flag = 0

        # 마지막 하나 남은 iv를 indexOrder에 추가해줘야 함
        if len(queue) == 0:
            indexOrder.append(iv)

        for q in queue:
            if v < q:
                queue.append(v)
                iQueue.append(iv)
                break
            else:
                flag += 1
                if flag == len(queue):
                    # order.append(v)
                    indexOrder.append(iv)
                    
    return indexOrder.index(location) + 1

# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))
# print(solution([3, 2, 4, 1, 1], 3))

# 런타임에러
print(solution([1, 1, 1], 0))