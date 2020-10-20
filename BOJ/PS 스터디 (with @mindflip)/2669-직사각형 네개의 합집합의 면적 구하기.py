import sys

inList = []
cdPlane = []
cnt = int(0)

# 2차원 리스트
for _ in range(100):
    line = []

    for _ in range(100):
        line.append(0)

    cdPlane.append(line)

# 입력
for _ in range(4):
    inList.append(list(map(int, sys.stdin.readline().split())))

# 풀이
for dots in inList:
    x1 = dots[0]
    y1 = dots[1]
    x2 = dots[2]
    y2 = dots[3]

    for x in range(x1, x2):
        for y in range(y1, y2):
            if cdPlane[x][y] == 0:
                cdPlane[x][y] += 1
                cnt += 1
            else:
                continue

print(cnt)

# 68 ms
# 아이디어 중요 -> 나중에 한 번 더 풀기