import sys

outList = []

in1 = int(sys.stdin.readline())
in2 = int(sys.stdin.readline())

strIn2 = str(in2)

outList.append(in1 * in2)

for ele in strIn2:
    outList.append(in1 * int(ele))

outList.reverse()

for ele in outList:
    print(ele)

# 64 ms