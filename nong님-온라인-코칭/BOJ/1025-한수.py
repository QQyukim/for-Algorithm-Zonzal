N = input()
n = int(N)
nList = []
hansu = int(0)
i = int(1)

while(i <= n):
    if len(N) == 1 or len(N) == 2:
        # 한 자리 or 두 자리
        hansu += 1
        i += 1

    elif len(N) == 3 or len(N) == 4:
        # 세 자리
        if i < 100:
            hansu += 1
            i += 1
        elif i >= 100 and i <= 999:
            nList = []                      # 초기화
            nList.append(i // 100)          # 백의 자리
            nList.append((i % 100) // 10)   # 십의 자리
            nList.append((i % 10))          # 일의 자리

            if nList[0] - nList[1] == nList[1] - nList[2]:
                hansu += 1
                i += 1
            else:
                i += 1
                continue
        else:
            break

print(hansu)