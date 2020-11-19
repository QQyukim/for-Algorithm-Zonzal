import sys
import math

n = int(sys.stdin.readline().strip())
aList = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
totalSV = 0

for a in aList:
    aMinusB = a - b
    if aMinusB < 0:
        deSV = 0
    else:
        deSV = math.ceil((a - b) / c)
    totalSV += 1 + deSV

print(totalSV)

# aMinusB 예외 처리 중요함!
# 828 ms