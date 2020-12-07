def solution(clothes):
    dic = {}
    answer = 1

    for el in clothes:
        name = el[0]
        kind = el[1]

        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1

    for v in dic.values():
        answer *= v + 1    

    answer = answer - 1
    return answer

# 한 종류당 입지 않은 것까지 모두 고려 (집합 생각)
# 종류가 같은 것끼리 묶어서 (ex) (hg + 1) * (ew + 1) - 1 로 계산
# 이 때 '+ 1'은 해당 옷을 안 걸칠 때를 뜻함

clothes1 = [['y_h', 'hg'], ["b_s", "ew"], ['g_t', 'hg']]
clothes2 = [['c_m', 'f'], ["b_s", "f"], ['s_m', 'f']]
print(solution(clothes1))