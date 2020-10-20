import sys

n = sys.stdin.readline().strip()

if len(n) == 2:
    res = int(n[0]) + int(n[1])
elif len(n) == 3: 
    if '0' in n[1]:
        res = 10 + int(n[2])
    elif '0' in n[2]:
        res = int(n[0]) + 10
else:
    res = 20

print(res)

# .strip() 작성 습관화!
# 68 ms