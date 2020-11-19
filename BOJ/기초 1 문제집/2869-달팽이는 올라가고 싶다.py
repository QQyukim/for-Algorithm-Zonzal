import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

# 계산식 먼저 세우기
distance = math.ceil(((v - a) / (a - b)) + 1)
print(distance)

# print(distance)

# 시간 초과
# while distance < height:
#     count += 1
    
#     distance += up
#     if distance >= height:
#         break
    
#     distance -= down

# 72 ms