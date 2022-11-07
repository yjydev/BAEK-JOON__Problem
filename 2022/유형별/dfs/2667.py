#단지번호붙이기
N = int(input())
board = [list(map(int,input())) for _ in range(N)]
res = []
visited = [[0]*N for _ in range(N)]
di = [0,0,1,-1]
dj = [1,-1,0,0]
arr = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (0 <= ni < N and 0 <= nj < N) and board[ni][nj] == 1:
                arr[i][j].append([ni,nj])

cnt = 1
def dfs(x,y):
    global cnt
    visited[x][y] = 1
    for nx,ny in arr[x][y]:
        if visited[nx][ny] == 0:
            cnt += 1
            visited[nx][ny] = 1
            dfs(nx,ny)

for a in range(N):
    for b in range(N):
        if board[a][b] == 1 and visited[a][b] == 0:
            dfs(a,b)
            res.append(cnt)
            cnt = 1

print(len(res))
print(*sorted(res))
