# bfs
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

# 변환할 수 없는 경우: 0 return
# 1. words 원소 중 begin과 두 글자가 같은 게 있으면 queue에 넣음
# 2. 한 글자씩 바꿔가며 target과 같은 게 나오는지 확인
# -> 바꿀 때마다 cnt 증가

from collections import deque

def solution(begin, target, words):
    queue = deque([[begin, 0]])

    while queue:
        vList = queue.popleft()
        bWord = vList[0]
        count = vList[1]
        count += 1
        
        # 각 알파벳 위치까지 고려해줘야함
        for word in words:
            sameCnt = 0
            for idx in range(len(bWord)):
                if bWord[idx] == word[idx]:
                    sameCnt += 1
            if sameCnt == len(begin) - 1:
                if target == word:
                    return count
                words.remove(word)
                queue.append([word, count])
    
    return 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
print(solution('hit', 'hhh', ['hht', 'hhh']))