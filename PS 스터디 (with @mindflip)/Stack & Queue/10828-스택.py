import sys

stack = []
answer = []

n = int(sys.stdin.readline().strip())

for _ in range(n):
    order = sys.stdin.readline().strip()

    if 'push' in order:
        el = int(order[5:])
        stack.append(el)
    
    elif order == 'pop':
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack.pop())

    elif order == 'size':
        answer.append(len(stack))

    elif order == 'empty':
        if len(stack) == 0:
            answer.append(1)
        else:
            answer.append(0)

    elif order == 'top':
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack[-1])

for el in answer:
    print(el)