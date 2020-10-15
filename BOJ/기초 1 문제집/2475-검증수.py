import sys

inList = []
sum = int(0)
result = int(0)
inList = list(map(int, sys.stdin.readline().split()))

for ele in inList:
    sum += ele ** 2

result = sum % 10
print(result)

# 64ms