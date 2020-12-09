import sys

stack = []
k = int(sys.stdin.readline().strip())
answer = 0

for _ in range(k):
    n = int(sys.stdin.readline().strip())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

for el in stack:
    answer += el

print(answer)