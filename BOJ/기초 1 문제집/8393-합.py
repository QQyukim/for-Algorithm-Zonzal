import sys

n = int(sys.stdin.readline())
sum = int(0)

while n > 0:
    sum += n
    n = n - 1

print(sum)

# 68ms