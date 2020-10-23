import sys

n = int(sys.stdin.readline().strip())
inList = list(map(int, sys.stdin.readline().split()))
l = len(inList)

inList.sort()

print(inList[0], inList[l-1])