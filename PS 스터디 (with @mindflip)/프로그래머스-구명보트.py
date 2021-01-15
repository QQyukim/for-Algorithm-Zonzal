# 한 번에 최대 2명씩 탈 수 있음, 무게 제한 있음
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출

# (처음 풀이: 효율성 테스트 모두 통과 못함)
# people 리스트를 내림차순으로 나열
# i가 people 리스트의 원소 수보다 작을 때 반복
#   가장 큰 값과 가장 작은 값의 합이 limit보다 작거나 같은 지?
#     -> 만약 가장 작은 값이 people[1]일 때 people[0]과 people[1] 삭제 후 answer 1 증가, i 초기화
#     -> 가장 작은 값이 people[1]이 아닐 때, i 증가하여 가리키는 값 변경, continue
#   가장 큰 값과 현재 가리키는 값의 합이 limit 보다 크다면
#     -> i가 1보다 큰 지 체크하여
#        해당 값의 이전 값과 가장 큰 값을 제거하고 answer += 1, i = 1 초기화
# 위 과정 후에 만약 people에 원소가 하나 이상 남아있다면 answer += 1
# (limit - 가장 큰 수) 값보다 작거나 같은 값이 list 원소 중 있는지 확인

# ------------------------------------------------------

# 리스트를 조정하면 O(n)의 시간복잡도 발생
# -> 인덱스 조회하는 방법 사용
def solution(people, limit):
    people = sorted(people)   # 내림차순
    startIdx = 0
    lastIdx = len(people) - 1
    answer = 0
    while startIdx < lastIdx:
        if people[startIdx] + people[lastIdx] <= limit:
            startIdx += 1
        lastIdx -= 1
        # 큰 수 쪽의 인덱스를 줄이면서 가장 작은 수와의 합을 limit와 비교
        answer += 1

    if startIdx == lastIdx:
        answer += 1
    return answer

print(solution([10, 20, 30, 40, 50], 100))
print(solution([10, 70, 50, 80, 50], 100))
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

# 효율성 테스트 1 통과 못함
# 가장 작지 않은 값과 가장 큰 값의 합이 limit을 넘지 않는 것까지 고려 안해도 되나?
def solutionF1(people, limit):
    people = sorted(people)   # 내림차순
    length = len(people)
    answer = 0
    while length > 0:
        minP = people.pop()
        length -= 1
        if length >= 1:
            maxP = people[0]
            if limit - minP >= maxP:
                people.remove(people[0])
                length -= 1
        answer += 1
    return answer

# 테스트케이스 모두 통과, 효율성 모두 통과 못함
# def solutionF1to5(people, limit):
#     answer = 0
#     i = 1
#     people = sorted(people, reverse=True)
#     while i < len(people):
#         if people[0] + people[len(people)-i] <= limit:
#             if i == len(people) - 1:
#                 people.remove(people[0])
#                 people.remove(people[len(people)-i])
#                 answer += 1
#                 i = 1
#             else:
#                 i += 1
#             continue
#         else:
#             if i > 1:
#                 people.remove(people[len(people)-(i-1)])
#             people.remove(people[0])
#             answer += 1
#             i = 1
#     if len(people) > 0:
#         answer += 1
#     return answer