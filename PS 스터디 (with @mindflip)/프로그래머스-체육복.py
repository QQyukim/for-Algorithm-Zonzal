#  바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다
#  전체 학생의 수 n
#  체육복을 도난당한 학생들의 번호가 담긴 배열 lost
#  여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
#  체육수업을 들을 수 있는 학생의 최댓값을 return

# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
# 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
# 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

# -----------------------------------

# =========>>>> 각 원소를 remove하지 않고 -1로 변경하는 풀이 (전처리 X)
# lost의 원소값(l) 조사
# l이 reserve에 있으면 reserve의 l 값을 -1으로 변경
#   + lost의 l 값을 -1으로 변경 
# l-1 이 reserve에 있으면 조사 종료
#     -> 만약 l-1이 lost에 있으면 안 빌려줌
#   -> l-1 값인 reserve의 원소값을 -1으로 변경
#   -> lost의 l 값 원소를 -1으로 변경
# l-1 이 reserve에 없으면 l+1 이 reserve에 있는지 조사
# -> 있으면: 조사 종료
#     -> 만약 l+1이 lost에 있으면 안 빌려줌
#   -> l+1 값인 reserve의 원소값을 -1으로 변경
#   -> lost의 l 값 원소를 -1으로 변경
# -> (그 외) 없으면: 못 빌려줌 -> continue
# -> lost에 -1 값이 있으면 체육복 없는 학생에 포함하지 않음

# ------------------------------------------------------------

# 처음: 전처리를 먼저 수행하지 않은 풀이
# lost를 기준으로 생각하니 복잡해짐
# 36~39 수행하지 않고 44~45, 47~48, 51~52 코드 살리고 46번째를 elif로 조건 걸면 케이스 7 실패

def solution(n, lost, reserve):
    # for i in range(1, n+1):
    #     if i in reserve and i in lost:
    #         reserve.remove(i)
    #         lost.remove(i)

    for l in lost:
        lIdx = lost.index(l)

        if l in reserve:
            rIdx = reserve.index(l)
        elif l-1 in reserve:
            if l-1 in lost:
                continue
            rIdx = reserve.index(l-1)
        elif l+1 in reserve:
            if l+1 in lost:
                continue
            rIdx = reserve.index(l+1)
        else:
            continue
        
        reserve[rIdx] = -1
        lost[lIdx] = -1

    lostCnt = len(lost) - lost.count(-1)
    answer = n - lostCnt

    return answer

# 전처리 안 한 풀이 2
# 케이스 7 성공 (50점)
def solutionEx(n, lost, reserve):
    # lost의 전처리 과정을 먼저 수행해야 케이스 7을 성공하는 듯...
    # 근데 reserve의 전처리도 같이 해야하는디
    # -> 어찌되었든 쓰레기 코드 (전처리를 무조건 먼저 해야함)

    # 전처리 쪽 코드가 잘못됨 (아래 3줄)
    # for r in reserve:
    #     if r in lost:
    #         lost.remove(r)

    # 수정
    for i in range(1, n+1):
        if i in reserve and i in lost:
            reserve.remove(i)
            lost.remove(i)

    for r in reserve:    
        if r-1 in lost:
            if r-1 in reserve:
                continue
            lost.remove(r-1)
        elif r+1 in lost:
            if r+1 in reserve:
                continue
            lost.remove(r+1)
        else:
            continue

    answer = n - len(lost)
    return answer

# 예시풀이 0
# def solution(n, lost, reserve):
#     answer = 0
#     for i in range(1, n+1):
#         if i not in lost: #안 잃어버린 학생
#             answer += 1
#         else:
#             if i in reserve: #잃어버렸지만 여분도 있는 학생
#                 answer += 1
#                 # 전처리 과정
#                 reserve.remove(i)
#                 lost.remove(i)

#     for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
#         if i-1 in reserve:
#             answer += 1
#             reserve.remove(i-1)

#         elif i+1 in reserve:
#             answer +=1
#             reserve.remove(i+1)

#     return answer


# 예시 풀이 1
def solutionEx1(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    return n - len(set_lost)

# 예시 풀이 2
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
# print(solution(5, [2], [2]))
# print(solution(5, [2, 5], [2]))
# print(solution(2, [1, 2], [1, 2]))
print(solution(5, [5, 4, 2], [2, 4]))
print(solution(3, [1, 2], [2, 3]))
print(solution(3, [1, 2, 3], [2, 3]))
print(solution(5, [3, 2, 1], [2, 3, 1]))