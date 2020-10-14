inList = []
dots = []
n = int(input())

for _ in range(n):
    inList = list(map(int, input().split()))
    dots.append(inList)

dots.sort(key = lambda x : (x[1], x[0]))

for dot in dots:
    print(dot[0], dot[1])

'''
# nong님 풀이

n = int(input())
arr = []

for i in range(n):
    x, y = map(int, input().split())
    arr.append((y, x))

arr.sort()

for (y, x) in arr:
    print(x, y)
'''