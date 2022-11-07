#DFS와 BFS
N,M,V = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
visited_d = [0] * (N+1)
visited_b = [0] * (N+1)

def dfs(n):
    visited_d[n] = 1
    print(n, end=' ')
    for w in sorted(arr[n]):
        if visited_d[w] == 0:
            visited_d[w] = 1
            dfs(w)

def bfs(n):
    visited_b[n] = 1
    queue = [n]
    print(n, end=' ')
    while queue:
        i = queue.pop(0)
        for w in sorted(arr[i]):
            if visited_b[w] == 0:
                print(w, end= ' ')
                queue.append(w)
                visited_b[w] = 1

dfs(V)
print()
bfs(V)