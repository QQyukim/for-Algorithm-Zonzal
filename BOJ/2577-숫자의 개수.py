inList = []
mulResult = int(1)
strMulResult = ""
cntDict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in range(3):
    inList.append(int(input()))

for i in range(3):
    mulResult *= inList[i]

strMulResult = str(mulResult)

for i in strMulResult:
    if i == '0':
        cntDict[0] += 1
    elif i == '1':
        cntDict[1] += 1
    elif i == '2':
        cntDict[2] += 1
    elif i == '3':
        cntDict[3] += 1
    elif i == '4':
        cntDict[4] += 1
    elif i == '5':
        cntDict[5] += 1
    elif i == '6':
        cntDict[6] += 1
    elif i == '7':
        cntDict[7] += 1
    elif i == '8':
        cntDict[8] += 1
    elif i == '9':
        cntDict[9] += 1

for i in range(10):
    print(int(cntDict[i]))