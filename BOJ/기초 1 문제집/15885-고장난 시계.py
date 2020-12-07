import sys

a, b = map(int, sys.stdin.readline().split())
answer = int(abs(1 - a/b) * 2)
print(answer)

# 1207
# t = 1
# broken = [0, 0, 0]
# normal = [0, 0, 0]
# count = 0

# 1130
# while t <= 86400:
#     if a / b >= 0:
#         bT = (a / b) * t
        
#     elif a / b < 0:
#         bT = 86400 + (a / b) * t
    
#     nT = t

#     broken[0] = bT // 3600
#     broken[1] = (bT % 3600) // 60
#     broken[2] = (bT % 3600) % 60

#     normal[0] = nT // 3600
#     normal[1] = (nT % 3600) // 60
#     normal[2] = (nT % 3600) % 60

#     if broken[0] == normal[0] or (broken[0] % 12) == (normal[0] % 12):
#         if broken[1] == normal[1] and broken[2] == normal[2]:
#             count += 1

#     t += 1

# print(count)