import sys

a, b, c, d = map(str, sys.stdin.readline().split())

abStr = a + b
cdStr = c + d

sum = int(abStr) + int(cdStr)
print(sum)

# 68 ms