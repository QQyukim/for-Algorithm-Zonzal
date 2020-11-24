import sys

m, d = map(int, sys.stdin.readline().split())
DaysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

for i in range(1, len(DaysOfMonth) + 1):
    if i != m:
        d += DaysOfMonth[i]
    else:
        break

if d % 7 == 0:
    print("SUN")
elif d % 7 == 1:
    print("MON")
elif d % 7 == 2:
    print("TUE")
elif d % 7 == 3:
    print("WED")
elif d % 7 == 4:
    print("THU")
elif d % 7 == 5:
    print("FRI")
elif d % 7 == 6:
    print("SAT")

# 68 ms