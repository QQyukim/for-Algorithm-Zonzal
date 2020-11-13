# 예시 입력값
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

# 로직
resultList = []
count = 0

for nth in moves:
    for i in range(len(board)):
        selected = board[i][nth - 1]
        if selected == 0:
            continue
        else:
            # 인형을 resultList에 넣고
            resultList.append(selected)
            # resultList를 탐색하여 같은 인형이 있는지 보기
            lenR = len(resultList)
            if lenR > 1:
                if resultList[lenR - 2] == resultList[lenR - 1]:
                    del resultList[lenR - 2:]
                    count += 2

            # 뽑힌 인형은 board에서 사라짐
            board[i][nth - 1] = 0
            break

# print(resultList)
print(count)
