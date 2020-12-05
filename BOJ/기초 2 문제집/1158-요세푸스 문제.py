import sys

# 원형 큐
cq = []
ans = []

n, k = map(int, sys.stdin.readline().split())
for i in range(n):
    cq.append(i+1)

front = 0

def deQueue(cq):
    global front
    front = (front + (k-1)) % len(cq)
    ans.append(cq[front])
    del cq[front]

while len(cq) > 0:
    deQueue(cq)

# print("<", end="")
# for i in range(len(ans)):
#     if i == len(ans) - 1:
#         print(ans[i], end=">")
#     else:
#         print(ans[i], end=", ")

print("<" + ", ".join(ans) + ">")