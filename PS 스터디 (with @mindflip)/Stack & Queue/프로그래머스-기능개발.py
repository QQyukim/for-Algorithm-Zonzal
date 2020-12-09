import sys
import math
from collections import deque

# 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도가 적힌 정수 배열 speeds
# 각 배포마다 몇 개의 기능이 배포되는지
# 배포는 하루에 한 번만 할 수 있음, 하루의 끝에 이루어짐
# --> 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

def solution(progresses, speeds):
    # Math.ceil((100 - p) / s)
    # count = 1부터 시작
    # 7, 3, 9 => v일차가 q일차보다 크면 q를 뱉고 count +=1, 작으면 count 뱉고 끝
    answer = []
    queue = deque()

    for i in range(len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while queue:
        count = 1
        v = queue.popleft()
        if v == 0:
            continue

        for i in range(len(queue)):
            if v >= queue[i]:
                queue[i] = 0
                count += 1
            else:
                break
        answer.append(count)
    
    return answer

p1 = [93, 30, 55]
s1 = [1, 30, 5]
p2 = [95, 90, 99, 99, 80, 99]
s2 = [1, 1, 1, 1, 1, 1]

print(solution(p1, s1))
print(solution(p2, s2))
