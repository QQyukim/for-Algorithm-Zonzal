import sys

# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이동 횟수 최소
# n개의 원판
# 장대: 3개

# 첫째 줄: 옮긴 횟수 k
# 두 번째 줄부터: 수행 과정 출력
# A B : A번째 탑의 가장 위에 있는 원판을
# ......B번째 탑의 가장 위로 옮긴다

def buildHanoi(n, fromPos, toPos, auxPos):
    global count
    count += 1

    if n == 1:
        posList.append((fromPos, toPos))
        return
    
    # 맨 밑 원판 제외한 원판들을 모두 auxPos에 옮긴다
    buildHanoi(n-1, fromPos, auxPos, toPos)
    
    # 맨 밑 원판을 목적지 기둥에 옮긴다
    posList.append((fromPos, toPos))
    
    # auxPos에 있는 원판들을 목적지 기둥에 옮긴다
    buildHanoi(n-1, auxPos, toPos, fromPos)

n = int(sys.stdin.readline().strip())
count = 0
posList = []

buildHanoi(n, 1, 3, 2)
print(count)

for ft in posList:
    print(ft[0], ft[1])