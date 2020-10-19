import sys

a, b = map(int, sys.stdin.readline().split())
res = int(0)
diff = abs(a - b)

if diff == 1:
    res = a + b
else:
    if diff % 2 == 0:
        res = int((a + b) * ((diff // 2) + 0.5))
    else:
        res = (a + b) * ((diff // 2) + 1)

print(res)

# 테스트를 잘 하고 제출하면 한 번에 통과 가능!
# 64 ms