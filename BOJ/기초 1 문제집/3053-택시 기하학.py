import sys
import math

n = int(sys.stdin.readline())
euclid = (n ** 2) * math.pi
taxi = (n ** 2) * 2

print(format(euclid, '.6f'))
print(format(taxi, '.6f'))

# 76 ms