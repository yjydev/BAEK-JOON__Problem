## 색종이   

N = int(input())
board = [[0 for i in range(100)] for j in range(100)]
for i in range(N):
    x, y = list(map(int,input().split(' ')))
    for r in range(y,y+10):
        for c in range(x,x+10):
            board[r][c] = 1
answer = 0
for i in range(100):
    answer += board[i].count(1)
print(answer)
