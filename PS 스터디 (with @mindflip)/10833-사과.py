import sys

n = int(sys.stdin.readline().strip())
inList = []
remApple = int(0)

for _ in range(n):
    inList.append(tuple(map(int, sys.stdin.readline().split())))

for school in inList:
    remApple += school[1] % school[0]

print(remApple)

#   68 ms