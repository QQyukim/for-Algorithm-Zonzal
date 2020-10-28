import sys

line = []
graph = []
maxDot = ()

for _ in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)

maxValue = graph[0][0]

for x in range(9):
    for y in range(9):
        if maxValue < graph[x][y]:
            maxValue = graph[x][y]
            maxDot = (x, y)
        else:
            continue

print(maxValue)
print(maxDot[0] + 1, maxDot[1] + 1)

# 64 ms