#유기농 배추
# dfs 로 재귀초과 발생

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int,input().split())
        board[y][x] = 1  # x <= M-1 / y <= N-1
    
    visited = [[0]*M for _ in range(N)]
    arr = [[[] for _ in range(M)] for _ in range(N)]
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    for i in range(N):
        for j in range(M):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if (0 <= ni < N and 0 <= nj < M) and board[ni][nj] == 1:
                    arr[i][j].append([ni,nj])
    
    def bfs(x,y):
        visited[x][y] = 1
        q = [[x,y]]
        while q:
            a,b = q.pop(0)
            for v,w in arr[a][b]:
                if visited[v][w] == 0:
                    q.append([v,w])
                    visited[v][w] = 1

    res = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                res += 1
    print(res)