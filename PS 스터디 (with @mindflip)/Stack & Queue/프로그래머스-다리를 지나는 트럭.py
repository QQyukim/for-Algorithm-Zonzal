import sys
from collections import deque

# solution(100, 100, [10,10,10,10,10,10,10,10,10,10])
def solution(bridge_length, weight, truck_weights):
    time = 1
    ingQueue = deque()
    sbQueue = deque(truck_weights)

    newT = sbQueue.popleft()
    ingQueue.append([newT, 1])

    while ingQueue:
        sumIng = 0
        for ingEl in ingQueue:
            ingEl[1] += 1

        if ingQueue[0][1] == bridge_length + 1:
            ingQueue.popleft()

        time += 1

        for ingEl in ingQueue:
            sumIng += ingEl[0]

        if len(sbQueue) > 0 and sumIng + sbQueue[0] <= weight:
            newT = sbQueue.popleft()
            ingQueue.append([newT, 1])
        else:
            continue

    return time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))