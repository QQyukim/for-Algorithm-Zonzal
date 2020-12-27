import sys
from itertools import permutations
# 순열

# 한 자리 숫자를 붙여 소수를 몇 개 만들 수 있는지?
# 011 과 11은 같음

# 모든 숫자 경우의 수 고려
# 소수 판별 구현

def solution(numbers):
    answer = 0
    ansList = []
    numList = []
    pList = []
    
    for el in numbers:
        numList.append(el)
    
    for i in range(1, len(numbers)+1):
        pList.append(list(permutations(numList, i)))
    
    # pList 내 중복제거
    for i in range(len(pList)):
        pList[i] = list(set(pList[i]))

    for idx in range(len(pList)):
        for pTuple in pList[idx]:
            # pList[idx]에는 원소 수가 idx+1 개인 pTuple가 있음
            strNum = ''
            for tOrder in range(len(pTuple)):
                strNum += pTuple[tOrder]
            number = int(strNum)

            # number을 일단 ansList에 넣어두고
            ansList.append(number)
            # number이 소수인지 아닌지 판별
            if number == 0 or number == 1:
                ansList.remove(number)
                continue
            else:
                # 제곱근까지 생각해도 됨!
                for i in range(2, (number // 2) + 1):
                    if number % i == 0:
                        ansList.remove(number)
                        break
    
    # ansList 내 중복제거
    ansList = list(set(ansList))

    answer = len(ansList)
    return answer

print(solution("17"))
print(solution("011"))

# 다른 사람 풀이
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)