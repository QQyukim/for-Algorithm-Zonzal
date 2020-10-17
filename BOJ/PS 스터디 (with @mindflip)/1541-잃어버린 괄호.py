import sys

inList = []
sum = int(0)

inList = sys.stdin.readline().strip().split('-')

for i in range(len(inList)):
    if '+' in inList[i]:
        sum = int(0)
        inList[i] = inList[i].split('+')
        for subEle in inList[i]:
            sum += int(subEle)
        inList[i] = sum
    else:
        continue

n = int(inList[0])  # int 변환해줘야 함
for i in range(1, len(inList)):
    n -= int(inList[i]) # int 변환해줘야 함

print(n)

# --- <주의점> ---
# line 8: order num 대신 element로 반복문 돌리면 ele = sum 대입 안 됨
# line 18, line 20: int 변환해줘야 함 (이유: 입력값으로 '05' 등 str 값이 들어올 수 있음)