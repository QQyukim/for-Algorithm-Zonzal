# 입력받은 값 공백 분리
#  map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환해줌

# 68ms
hour, minute = map(int, input().split())
timerMin = int(input())

minute += timerMin

if minute >= 60:
    hour += minute // 60
    minute = minute % 60 

if hour >= 24:
    hour -= 24

print(hour, minute)

"""
# 다른 사람 풀이 # 64ms

H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)
"""

"""
a, b = map(int, input().split())
c = int(input())

d = int(0)
e = int(0)

if c >= 60:
    d = a + int(c // 60)
    if d >= 24:
        d = d - 24
    
    e = b + int(c % 60)
    if e >= 60:
        d += e // 60
        e = e % 60
else:
    d = a
    e = b + c

    if e >= 60:
        d = a + int(e // 60)
        e = e % 60

        if d >= 24:
            d = d - 24

print(d, e)

"""