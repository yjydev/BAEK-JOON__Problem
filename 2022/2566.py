# 최대값    

answer = 0
x, y = 0, 0
for i in range(9):
    board = list(map(int,input().split(' ')))
    tmp = max(board)
    if tmp > answer:
        answer = tmp
        x = i
        y = board.index(answer)
print(answer)
print(x+1,y+1)

#-------------------

# 기존 풀이 
# board = [list(map(int, input().split(' '))) for i in range(9)]
# answer = board[0][0]
# pos = [0,0]
# for i in range(9):
#     for j in range(9):
#         if answer < board[i][j]:
#             pos = [i,j]
#             answer = board[i][j]
# print(answer)
# print(pos[0]+1, pos[1]+1)
