import sys

def solution(answers):
    answer = []

    firstSPJ = [1,2,3,4,5]
    secondSPJ = [2,1,2,3,2,4,2,5]
    thridSPJ = [3,3,1,1,2,2,4,4,5,5]

    dict_count = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):
        num = i % len(firstSPJ)
        if answers[i] == firstSPJ[num]:
            dict_count[1] += 1
    
        num = i % len(secondSPJ)
        if answers[i] == secondSPJ[num]:
            dict_count[2] += 1
    
        num = i % len(thridSPJ)
        if answers[i] == thridSPJ[num]:
            dict_count[3] += 1

    # 최댓값 구하기
    maxCount = max(dict_count[1], dict_count[2], dict_count[3])
    for key in dict_count:
        if maxCount == dict_count[key]:
            answer.append(key)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))