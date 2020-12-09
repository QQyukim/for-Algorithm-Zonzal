import sys
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        count = 0
        v = queue.popleft()

        for q in queue:
            count += 1
            if v > q:
                break
        answer.append(count)
    
    return answer

# 시간 초과
# def solution(prices):
#     answer = []
#     queue = deque(prices)
#     while queue:
#         count = 0
#         v = queue.popleft()

#         for i in range(len(queue)):
#             count += 1
#             if v > queue[i]:
#                 break
#         answer.append(count)
    
#     return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
# [4, 3, 1, 1, 0]