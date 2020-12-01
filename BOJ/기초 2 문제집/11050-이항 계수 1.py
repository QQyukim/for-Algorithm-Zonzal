import sys
# from math import factorial

def f(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    return num * f(num - 1)

n, k = map(int, sys.stdin.readline().split())

biCo = f(n) / ( f(k) * f(n - k) )
print(int(biCo))

# 72 ms