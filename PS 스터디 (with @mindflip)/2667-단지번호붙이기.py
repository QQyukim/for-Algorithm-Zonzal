import sys

graph = []
result = []
cnt = 0

def dfs(x, y):
    global cnt    # 전역변수

    if x < 0  or x >= n or y < 0 or y >= n:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        cnt += 1
        return True
    return False

n = int(sys.stdin.readline().strip())

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

for x in range(n):
    for y in range(n):
        if dfs(x, y) == True:
            result.append(cnt)
            cnt = 0

result.sort()

print(len(result))
for ele in result:
    print(ele)