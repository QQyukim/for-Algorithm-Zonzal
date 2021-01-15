# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.

# number를 배열로 만들어 len(number) - k 의 '조합' 생성
# 조합끼리 수 비교하여 max 값 찾기

def solution(number, k):
    answer = ''
    stack = [number[0]]

    for n in number[1:]:    # 순서대로 탐색
        while len(stack) > 0 and stack[-1] < n and k > 0:
            # 값을 한개 빼서 k는 1이 제거 
            k -= 1
            # 내부의 값을 제거 
            stack.pop()
        # 새로운 값을 삽입 
        stack.append(n)

    if k != 0:
        stack = stack[:-k]

    answer = ''.join(stack)
    return answer

# 시간 초과
# from itertools import combinations
# def solution(number, k):
#     answer = ''
#     pickedLen = len(number) - k
#     cList = []
#     for i in list(combinations(number, pickedLen)):
#         cList.append(i)
#     maxAns = 0
#     for c in cList:
#         strNumber = ''
#         n = 0
#         for cEl in c:
#             strN += cEl
#         n = int(strN)
#         maxAns = max(maxAns, n)
#     answer = str(maxAns)
#     return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))