import sys

l, p = map(int, sys.stdin.readline().split())
npList = []

npList = list((map(int, sys.stdin.readline().split())))

mul = l * p

for ele in npList:
    diff = ele - mul
    print(diff, end=' ')

# 60 ms