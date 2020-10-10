numDots = int(input())
dots = []

for i in range(numDots):
    x, y = map(int, input().split())
    dots.append((x, y))    # tuple

dots.sort()

for i in dots:
    print(i[0], i[1])
    

# 시간초과 메세지
'''
numDots = int(input())
x = []
y = []

for i in range(numDots):
    xx, yy = map(int, input().split())

    x.append(xx)
    y.append(yy)

for i in range(numDots - 1):
    for i in range(numDots - 1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
            y[i], y[i+1] = y[i+1], y[i]    # y와 x의 원소 개수는 항상 같음

        if x[i] == x[i+1]:
            if y[i] > y[i+1]:
                y[i], y[i+1] = y[i+1], y[i]

for i in range(numDots):
    print(x[i], y[i])
'''