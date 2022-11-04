N = int(input())
board = [list(map(int,input())) for _ in range(N)]
arrList = [[[] for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

di = [1,-1,0,0]
dj = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (0 <= ni < N and 0 <= nj < N) and board[ni][nj] != 0:
                arrList[i][j].append([ni, nj])
def bfs(n):
    q = []
    q.append(n)
    result = 1
    while q:
        s1,s2 = q.pop(0)
        for w1,w2 in arrList[s1][s2]:
            if visited[w1][w2] == 0:
                q.append([w1,w2])
                visited[w1][w2] = visited[s1][s2]
                result += 1
    return result
cnt = 0
num = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            visited[i][j] = cnt
            num.append(bfs([i,j]))

print(cnt)
num.sort()
print('\n'.join(map(str,num)))

# 처음에 오름차순 정렬 안해서 틀렸었음





