# KMP는 왜 KMP일까?

longWord = input()
abb = longWord[0]

for i in range(len(longWord)):
    if (longWord[i] == '-'):
        abb += longWord[i+1]

print(abb)

# 대문자나 하이픈(아스키코드)는 신경을 쓰지 않나?
# 신경 쓴 코드 만들어보기?