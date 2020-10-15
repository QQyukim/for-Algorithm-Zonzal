import sys

inSec = int(0)

for _ in range(4):
    inSec += int(sys.stdin.readline())

min = inSec // 60
sec = inSec % 60

print(min)
print(sec)

# 68 ms