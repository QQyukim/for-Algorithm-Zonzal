import sys

x, y, w, h = map(int, sys.stdin.readline().split())

if x >= w / 2:
    diffWidth = w - x
else:
    diffWidth = x

if y >= h / 2:
    diffHeight = h - y
else:
    diffHeight = y

minDist = min(diffWidth, diffHeight)

print(minDist)