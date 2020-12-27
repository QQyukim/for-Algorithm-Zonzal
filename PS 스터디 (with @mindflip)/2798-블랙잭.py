import sys
from itertools import combinations

# 카드 합 <= 21, 카드 합 최대한 크게!
# -> 합 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합

n, m = map(int, sys.stdin.readline().split())
cardList = list(map(int, sys.stdin.readline().split()))
best = 0

threeCards = list(combinations(cardList, 3))

for tEl in threeCards:
    if 0 < sum(tEl) <= m:
        # m 이하의 가장 큰 수를 구하면 됨!
        best = max(best, sum(tEl))

print(best)