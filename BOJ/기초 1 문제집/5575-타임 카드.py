import sys

a = []
b = []
c = []

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))


def findWorkTime(inList):
    h1 = inList[0]
    m1 = inList[1]
    s1 = inList[2]
    h2 = inList[3]
    m2 = inList[4]
    s2 = inList[5]

    s = s2 - s1
    m = m2 - m1
    h = h2 - h1

    if s < 0:
        m = m - 1
        s = 60 + s
    if m < 0:
        h = h - 1
        m = 60 + m
    
    return h, m, s

resAh, resAm, resAs = findWorkTime(a)
resBh, resBm, resBs = findWorkTime(b)
resCh, resCm, resCs = findWorkTime(c)

print(resAh, resAm, resAs)
print(resBh, resBm, resBs)
print(resCh, resCm, resCs)

# 64 ms