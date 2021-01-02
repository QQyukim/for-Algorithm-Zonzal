# 암호: 서로 다른 L개의 알파벳 소문자들로 구성
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
# 암호를 이루는 알파벳이 암호에서 '증가'하는 순서로 배열

# 암호로 쓸 법한 문자 종류: C가지
# C개의 문자가 주어졌을 때, 가능성 있는 암호를 모두 구하라

# input: L, C
# output: 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력

import sys
from itertools import combinations

def function(lenMo, lenJa):
    moComList = []
    jaComList = []
    if lenMo < 1:
        return
    else:
        if lenJa < 2:
            return
        else:
            for m in range(1, lenMo + 1):
                if l - m < 2:
                    continue
                else:
                    moComList.append(list(combinations(moList, m)))
                    jaComList.append(list(combinations(jaList, l - m)))

            newCom = ()
            newComList = []
            for idx in range(len(moComList)):
                for moTuple in moComList[idx]:
                    for jaTuple in jaComList[idx]:
                        newStr = ''
                        newCom = moTuple + jaTuple
                        for newComEle in newCom:
                            newStr += newComEle
                        newStr = ''.join(sorted(newStr))
                        newComList.append(newStr)

            newComList = sorted(newComList)
            for el in newComList:
                print(el)

l, c = map(int, sys.stdin.readline().split())
alphabetList = list(map(str, sys.stdin.readline().split()))
moCount = 0
moList = []
jaList = []

for alphabet in alphabetList:
    if alphabet in ['a', 'e', 'i', 'o', 'u']:
        moCount += 1
        moList.append(alphabet)
    else:
        jaList.append(alphabet)

lenMo = len(moList)
lenJa = len(jaList)

function(lenMo, lenJa)
# 72 ms

# 다른 사람 풀이
# import sys
# from itertools import combinations

# vowels = ['a', 'e', 'i', 'o', 'u']
# L, C = map(int, sys.stdin.readline().split())
# pwd = sorted(list(map(str, sys.stdin.readline().split())))

# comb = combinations(pwd, L)

# for c in comb:
#     count = 0
#     for letter in c:
#         if letter in vowels:
#             count += 1

#     if (count >= 1) and (count <= L-2):
#         print(''.join(c))