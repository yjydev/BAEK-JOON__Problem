def bfs(n):
    que = []
    que.append(n)
    visited[n[0]][n[1]] = 1
    while que:
        x,y = que.pop(0)
        if [x,y] == target:
            break
        else:
            for k in range(8):
                nx = x + di[k]
                ny = y + dj[k]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx,ny])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    now = list(map(int,input().split()))
    target = list(map(int,input().split()))
    visited = [[0] * N for _ in range(N)]
    di = [-2,-1,1,2,2,1,-2,-1]
    dj = [1,2,2,1,-1,-2,-1,-2]
    bfs(now)
    print(visited[target[0]][target[1]]-1)