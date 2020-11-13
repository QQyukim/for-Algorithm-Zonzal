import sys

n = int(sys.stdin.readline().strip())
testNumList = []

for _ in range(n):
    testNumList.append(int(sys.stdin.readline().strip()))

for num in testNumList:
    count = 0
    # 5일 때 문 6개 생성
    doors = [0 for _ in range(num + 1)]

    # len(door) = 6
    for index in range(1, len(doors)):
        for k in range(1, num + 1):
            if index % k == 0:
                doors[index] += 1
    
    for eachDoor in doors:
        if eachDoor % 2 == 1:
            count += 1
    
    print(count)

# 104 ms

