import sys

a, b, c, x, y = map(int, sys.stdin.readline().split())

if (a + b) < (2 * c):
    price = (a * x) + (b * y)
else:
    price = (min(x, y) * (2 * c))
    if x > y:
        price += (x - y) * min(a, 2 * c)
    elif x < y:
        price += (y - x) * min(b, 2 * c)

print(price)

# 68 ms