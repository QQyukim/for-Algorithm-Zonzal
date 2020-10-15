import sys

inSec = int(sys.stdin.readline())
aCnt = int(0)
bCnt = int(0)
cCnt = int(0)

if (inSec % 10) == 0:
    aCnt += inSec // 300
    inSec = inSec % 300

    bCnt += inSec // 60
    inSec = inSec % 60

    cCnt += inSec // 10

    print(aCnt, end=' ')
    print(bCnt, end=' ')
    print(cCnt)
else:
    print(-1)

# 문제를 잘 읽자
# 64 ms