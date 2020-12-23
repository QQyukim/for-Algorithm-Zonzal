def solution(brown, yellow):
    answer = []
    # yw, yh
    # yw * yh == yellow
    # 정답: yw+2, yh+2

    if yellow == 1:
        answer = [3, 3]
    else:
        for yw in range(1, yellow // 2 + 1):
            for yh in range(1, yellow // yw + 1):
                if yw * yh == yellow:
                    aroundY = 4 + ((yw + yh) * 2)
                    if aroundY == brown:
                        answer = [yw + 2, yh + 2]
                        answer = sorted(answer, reverse=True)

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))