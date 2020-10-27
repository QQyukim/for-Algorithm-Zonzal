'''
# 1
def solution(phone_book):
    for ele1 in phone_book:
        for ele2 in phone_book:
            if ele1 == ele2:
                continue
            else:
                if ele1 in ele2:
                    answer = False
                    return answer
                else:
                    answer = True
    
    return answer
'''
# phone_book에 중복되는 값이 있으면 위 코드는 틀림

'''
# 2
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j:
                continue
            else:
                if phone_book[i] in phone_book[j]:
                    answer = False
                    return answer
                else:
                    answer = True
    
    return answer
'''
# 문자열 in 문자열 => 접두사가 아니고 포함만 되어도 False가 뜲

# 3 - 정답
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j:
                continue
            else:
                l = len(phone_book[i])
                if phone_book[i] in phone_book[j][0:l]:
                    answer = False
                    return answer
                else:
                    answer = True
    
    return answer

phone_book1 = ['119', '123456', '119230583']
phone_book2 = ['123', '456', '789']
phone_book3 = ['12', '123', '1235', '567', '88']
phone_book3 = ['12', '12', '1234', '567', '88']

# print(solution(phone_book1))
# print(solution(phone_book2))
print(solution(phone_book3))