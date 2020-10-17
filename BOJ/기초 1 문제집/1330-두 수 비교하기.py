import sys

a, b = map(int, sys.stdin.readline().split())

if a > b:
    print(">")
elif a == b:
    print("==")
elif a < b:
    print("<")

# 60 ms