import sys

n = int(sys.stdin.readline())

res = n % 8

if res == 6:
    res = 4
elif res == 7:
    res = 3
elif res == 0:
    res = 2

print(res)

# 72 ms