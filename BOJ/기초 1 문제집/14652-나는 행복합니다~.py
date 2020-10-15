import sys

n, m, sNum = map(int, sys.stdin.readline().split())

b = sNum % m
a = sNum // m

print(a, end=' ')
print(b)

# 68 ms