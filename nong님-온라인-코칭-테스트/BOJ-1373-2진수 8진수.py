binStr = input()
binList = []
i = int(0)
dec = int(0)
octList = []
octStr = ''
octInt = int(0)

# binStr 쪼개서 리스트에 넣기
while i < len(binStr):
    binList.append(binStr[i:i+1])
    i += 1

binList.reverse()
i = int(0)

# 2진수 -> 10진수
while i < len(binStr):
    dec += (2 ** i) * int(binList[i])
    i += 1

# 10진수 -> 8진수
while 1:
    octList.append(str(dec % 8))
    dec = dec // 8
    if dec == 0:
        break

octList.reverse()

for i in octList:
   octStr += i

octInt += int(octStr)

print(octInt)