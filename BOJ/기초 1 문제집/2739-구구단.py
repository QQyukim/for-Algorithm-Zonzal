import sys

n = int(sys.stdin.readline().strip())

for i in range(1, 10):
    print(n, '*', i, '=', n * i)

# 64 ms