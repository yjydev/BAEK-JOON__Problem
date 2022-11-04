N = int(input())    # 정점 개수(사람 수)
S, E = map(int, input().split())    # 시작, 끝
m = int(input())    # 간선 개수
edge = [list(map(int, input().split())) for _ in range(m)]
visited = [-1] * (N+1)
adjList = [[]*(N+1) for _ in range(N+1)]
for i in range(m):
    n1 , n2 = edge[i][0], edge[i][1]
    adjList[n1].append(n2)
    adjList[n2].append(n1)
def bfs(s,v):
    q = []
    q.append(s)
    visited[s] = 0
    while q:
        t = q.pop(0)
        for w in adjList[t]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[t] + 1
            if w == v:
                return visited[w]
    return -1
print(bfs(S,E))
            

