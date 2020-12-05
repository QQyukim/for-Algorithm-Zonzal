import sys

dish_list = list(sys.stdin.readline().strip())
ans = 10

for i in range(1, len(dish_list)):
    if dish_list[i-1] == dish_list[i]:
        ans += 5
    else:
        ans += 10

print(ans)

# 문자열보다 리스트가 처리 시간이 더 빠름