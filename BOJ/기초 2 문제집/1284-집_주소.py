# 각 숫자 사이에는 1cm의 여백이 들어가야한다.
# 1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다.
# 나머지 숫자는 모두 3cm의 너비를 차지한다.
# 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.

import sys

n = ''
while True:
    n = sys.stdin.readline().strip()

    if n == '0':
        break
    else:
        width = 2
        for sub in n:
            if sub == '1':
                width += 2
            elif sub == '0':
                width += 4
            else:
                width += 3
        
        width += len(n) - 1
        print(width)