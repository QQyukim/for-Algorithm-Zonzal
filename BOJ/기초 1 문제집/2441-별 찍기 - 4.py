import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    print(' ' * i, end='')
    print('*' * (n - i))

# 64 ms