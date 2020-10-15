import sys

corrSet = [1, 1, 2, 2, 2, 8]
inSet = []

inSet = list(map(int, sys.stdin.readline().split()))

for i in range(len(corrSet)):
    print(corrSet[i] - inSet[i], end=' ')

# 68 ms