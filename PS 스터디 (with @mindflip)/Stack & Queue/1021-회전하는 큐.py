import sys
from collections import deque

# 큐에 포함된 수 N
# 뽑아내려고 하는 수 개수 M (M <= N)
# 지민이가 뽑아내려고 하는 원소의 위치
# (가장 처음 큐에서의 위치)
# 1 <= 위치 <= N

# 2번 연산: 왼쪽으로 이동
# 3번 연산: 오른쪽으로 이동

n, m = map(int, sys.stdin.readline().split())
popList = list(map(int, sys.stdin.readline().split()))

count = 0
popQueue = deque(popList)
queue = deque([ i for i in range(1, n + 1) ])

while popQueue:
    v = popQueue[0]
    qLen = len(queue)
    qIdx = queue.index(v)

    if v == queue[0]:
        queue.popleft()
        popQueue.popleft()
        continue
    else:
        count += 1
        if qIdx < qLen / 2:
            il = queue.popleft()
            queue.append(il)
        else:
            ir = queue.pop()
            queue.appendleft(ir)

print(count)
