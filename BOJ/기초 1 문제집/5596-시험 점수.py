import sys

mgList = []
msList = []
s = int(0)
t = int(0)

mgList = list(map(int, sys.stdin.readline().split()))
msList = list(map(int, sys.stdin.readline().split()))

for i in range(4):
    s += mgList[i]
    t += msList[i]

if s == t:
    print(s)
else:
    print(max(s, t))

# 64 ms