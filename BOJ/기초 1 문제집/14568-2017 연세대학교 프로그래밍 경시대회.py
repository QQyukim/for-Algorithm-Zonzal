import sys

n = int(sys.stdin.readline().strip())
setCount = 0

for a in range(2, n - 1, 2):
    for b in range(1, n - 1):
        x = n - a - (2 * b)
        if x >= 2:
            setCount += 1
        else:
            continue

print(setCount)

# 76 ms

# 어떤 (b,c) 쌍은 특정 a에 대하여 1쌍만 존재함
# 남규 >= 영훈 + 2
# b에 초점 맞추기 (아래)

# for a in range(2, n - 1, 2):
#     setCount += (n - a - 2) // 2  # -2: 2개 미리 빼놓기