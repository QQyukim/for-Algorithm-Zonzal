# 파이썬 딕셔너리 쌍 추가하기 => 활용!
# 풀이 참고 (https://eda-ai-lab.tistory.com/472)

def solution(clothes):
    answer = {}

    for ele in clothes:
        if ele[1] in answer:
            answer[ele[1]] += 1
        else:
            answers[ele[1]] = 1

    # {'hg': 2, 'ew': 1}
    
    cnt = 1
    for value in answer.values():
        cnt *= (value + 1)
    
    return cnt - 1

    # 한 종류당 입지 않은 것까지 모두 고려 (집합 생각)
    # 종류가 같은 것끼리 묶어서 (ex) (hg + 1) * (ew + 1) - 1 로 계산
    # 이 때 '+ 1'은 해당 옷을 안 걸칠 때를 뜻함

clothes1 = [['y_h', 'hg'], ["b_s", "ew"], ['g_t', 'hg']]
clothes2 = [['c_m', 'f'], ["b_s", "f"], ['s_m', 'f']]
print(solution(clothes1))