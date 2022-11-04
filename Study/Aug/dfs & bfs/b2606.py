N = int(input()) # 컴퓨터 수
V = int(input()) # 간선 수
edge = [list(map(int,input().split())) for _ in range(V)]
adjList = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(V):
    n1, n2 = edge[i][0], edge[i][1]
    adjList[n1].append(n2)
    adjList[n2].append(n1)

def bfs(s):
    cnt = 0
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop()
        for w in adjList[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
                cnt += 1
    return cnt

print(bfs(1))









