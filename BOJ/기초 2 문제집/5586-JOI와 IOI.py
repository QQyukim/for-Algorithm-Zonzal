import sys

word = sys.stdin.readline().strip()
joiCnt = 0
ioiCnt = 0

for i in range(len(word) - 2):
    if 'JOI' == word[i:i+3]:
        joiCnt += 1
    elif 'IOI' == word[i:i+3]:
        ioiCnt += 1
    else:
        continue

print(joiCnt)
print(ioiCnt)

# 76 ms