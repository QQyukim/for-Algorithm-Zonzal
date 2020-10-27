import sys

inList = []
outList = []
T = int(sys.stdin.readline().strip())

for i in range(T):
    inList.append(tuple(map(int, sys.stdin.readline().split())))

    W = inList[i][0]
    H = inList[i][1]
    N = inList[i][2]

    Y = N // W
    X = N % W

    if X == 0:
        X = str(W)
    else:
        Y = Y + 1
        X = str(X)

    if Y < 10:
        Y = '0' + str(Y)
    else:
        Y = str(Y)
    
    outList.append(X + Y)

for ele in outList:
    print(ele)

# 80 ms