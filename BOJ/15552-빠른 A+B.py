import sys

inList = []

n = int(sys.stdin.readline())
for _ in range(n):
    inList.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(len(inList)):
    print(inList[i][0] + inList[i][1])

# sys.stdin.readline() 풀이: 1956ms
# input() 풀이: 시간 초과