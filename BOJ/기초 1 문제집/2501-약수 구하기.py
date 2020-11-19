import sys

n, k = map(int, sys.stdin.readline().split())
num = 1
count = 0
ans = 0

while num <= n:
    if n % num == 0:
        count += 1
        if count == k:
            ans = num
            break
    num += 1

print(ans)

# 80 ms