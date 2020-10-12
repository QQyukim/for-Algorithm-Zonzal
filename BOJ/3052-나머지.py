inList = []
rList = []
count = int(0)

for i in range(10):
    inList.append(int(input()))

for num in inList:
    rList.append(num % 42)

count += len(list(set(rList)))

print(count)