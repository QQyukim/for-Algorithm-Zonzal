import sys
import math

n = int(sys.stdin.readline().strip())

minTime = math.ceil(n / 5)

if minTime == 0:
    minTime = 1

print(minTime)

# 68 ms