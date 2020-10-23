import sys

n = int(sys.stdin.readline().strip())

for i in range(n , 0 , -1):
    print(' ' * (i - 1) , end='')
    print('*' * (2 * (n - i) + 1))

# 72 ms