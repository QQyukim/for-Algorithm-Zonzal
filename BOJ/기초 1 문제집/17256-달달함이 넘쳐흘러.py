import sys

ax, ay, az = map(int, sys.stdin.readline().split())
cx, cy, cz = map(int, sys.stdin.readline().split())

bx = cx - az
by = cy // ay
bz = cz - ax

print(bx, end=' ')
print(by, end=' ')
print(bz)

# 68 ms