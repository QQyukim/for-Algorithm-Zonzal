import sys

count = 0
plate = []
for line in range(8):
    plate.append(list(sys.stdin.readline().strip()))

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and plate[i][j] == 'F':
            count += 1
        elif i % 2 == 1 and j % 2 == 1 and plate[i][j] == 'F':
            count += 1

print(count)