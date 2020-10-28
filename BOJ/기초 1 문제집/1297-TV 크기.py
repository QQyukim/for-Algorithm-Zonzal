import sys
import math

n, a, b = map(int, sys.stdin.readline().split())

x = math.sqrt(float( (n ** 2) / ((a ** 2) + (b ** 2))))

ax = int(math.floor(a * x))
bx = int(math.floor(b * x))

print(ax, bx)

# 80 ms