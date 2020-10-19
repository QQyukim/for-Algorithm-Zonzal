import sys

m = int(sys.stdin.readline())
d = int(sys.stdin.readline())
res = ""

if m == 1:
    res = "Before"
elif m == 2:
    if d < 18:
        res = "Before"
    elif d == 18:
        res = "Special"
    elif 18 < d <= 31:
        res = "After"
elif 3 <= m <= 12:
    res = "After"

print(res)

# 64 ms