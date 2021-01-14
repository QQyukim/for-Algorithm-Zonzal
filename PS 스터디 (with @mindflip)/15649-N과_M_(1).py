# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# -> 순열

import sys
from itertools import permutations

n, pick = map(int, sys.stdin.readline().split())
items = [i for i in range(1, n+1)]
p = []

for i in list(permutations(items, pick)):
  p.append(i)

for pEl in p: # pEl: tuple
  for i in range(len(pEl)):
    print(pEl[i], end=' ')
  print()