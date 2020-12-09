import sys

n = int(sys.stdin.readline().strip())
answer = []

for _ in range(n):
    stack = []
    ps = sys.stdin.readline().strip()

    if ps[0] == ')':
        answer.append('NO')
        continue

    for i in range(len(ps)):
        stack.append(ps[i])
        
        if len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
        
    if len(stack) == 0:
        answer.append('YES')
    else:
        answer.append('NO')

for el in answer:
    print(el)