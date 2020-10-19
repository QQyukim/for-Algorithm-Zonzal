import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

sum1 = a + d
sum2 = b + c

print(min(sum1, sum2))

# 64ms