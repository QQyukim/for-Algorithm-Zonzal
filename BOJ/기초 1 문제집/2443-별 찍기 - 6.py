import sys

n = int(sys.stdin.readline().strip())

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * ((i * 2) - 1))