import sys

inList = []

for _ in range(5):
    inList.append(int(sys.stdin.readline()))

a = inList[0]
b = inList[1]
c = inList[2]
d = inList[3]
p = inList[4]

x = p * a

if p <= c:
    y = b
else:
    y = b + (p - c) * d

res = min(x, y)
print(res)

# 64 ms