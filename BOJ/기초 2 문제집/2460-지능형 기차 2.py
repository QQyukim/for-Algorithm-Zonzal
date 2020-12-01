import sys

train = []
people = 0
maxPeople = 0

for _ in range(10):
    off, on = map(int, sys.stdin.readline().split())
    train.append([off, on])

for cabin in train:
    people -= cabin[0]
    people += cabin[1]

    maxPeople = max(people, maxPeople)

print(maxPeople)

# 72 ms