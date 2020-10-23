import sys

n, x = map(int, sys.stdin.readline().split())
aList = list(map(int, sys.stdin.readline().split()))

for a in aList:
    if a < x:
        print(a, end=" ")

# 80 ms