
def dfs(s,cnt):
    global end, res
    if cnt > K :
        return
    i,j = s
    if s == end:
        if cnt == K :
            res += 1
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
            if board[ni][nj] == '.':
                visited[ni][nj] = 1
                dfs([ni,nj],cnt+1)
                visited[ni][nj] = 0



R,C,K = map(int,input().split())
board = [list(input()) for _ in range(R)]
visited = [[0] * (C+1) for _ in range(R+1)]
di = [0,0,-1,1]
dj = [-1,1,0,0]
start = [R-1,0]
end = [0,C-1]
res = 0
visited[R-1][0] = 1
dfs(start,1)
print(res)
