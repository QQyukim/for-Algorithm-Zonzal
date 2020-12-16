import sys

t = int(sys.stdin.readline().strip())
cntList = []

for _ in range(t):
    # 그리드 생성
    grid = []
    n, m = map(int, sys.stdin.readline().split())
    for row in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))

    # 특정 col 아래에 박스가 쌓인 개수 구해야 함
    # col 기준으로 row 큰 수부터 작은 수로 탐색
    count = 0
    for col in range(m):
        box = 0
        for row in range(n-1, -1, -1):
            if grid[row][col] == 1:
                count += (n-1) - row - box
                box += 1
    
    cntList.append(count)

for el in cntList:
    print(el)