# 두 개 이상 리스트의 모든 조합 구하기
from itertools import product

# 예시 입력
numbers = [1,1,1,1,1]
target = 3

# 로직
count = 0
items = [(ele, -ele) for ele in numbers]

combiList = list(product(*items))

for nTuple in combiList:
    if sum(nTuple) == target:
        count += 1

print(count)