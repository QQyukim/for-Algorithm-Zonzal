inList = []
outList = []

num = int(input())
inList = list(map(int, input().split()))

# inList에서 중복값 바로 쳐내기
outList = sorted(list(set(inList)))

for i in outList:
    print(i, end=' ')