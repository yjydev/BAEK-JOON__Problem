#섬의 개수
# 대각선 포함 => 8방향
while True:
    w, h = map(int,input().split())
    if w == h == 0:
        break
    board = [list(map(int,input().split())) for _ in range(h)]
    di = [0,0,1,-1,1,1,-1,-1]
    dj = [1,-1,0,0,1,-1,1,-1]
    arr = [[[] for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            for k in range(8):
                ni = i+di[k]
                nj = j+dj[k]
                if (0<=ni<h and 0<=nj<w) and board[ni][nj] == 1:
                    arr[i][j].append([ni,nj])
    visited = [[0]*w for _ in range(h)]
    def bfs(x,y):
        q = [[x,y]]
        visited[x][y] = 1
        while q:
            i,j = q.pop(0)
            for v,w in arr[i][j]:
                if visited[v][w] == 0:
                    q.append([v,w])
                    visited[v][w] = 1
    res = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                res += 1
    print(res)
