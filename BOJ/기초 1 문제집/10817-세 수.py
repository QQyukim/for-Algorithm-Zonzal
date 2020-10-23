import sys

inList = []

inList = list(map(int, sys.stdin.readline().split()))
l = len(inList)

inList.sort()
print(inList[l-2])

# 72 ms