#연결 요소의 개수
# dfs 재귀초가오류
import sys
N,M = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0]*(N+1)

def bfs(n):
    q = [n]
    visited[n] = 1
    while q:
        v = q.pop(0)
        for w in arr[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1

res = 0
for i in range(1,N+1):
    if visited[i] == 0:
        bfs(i)
        res += 1
print(res)

# def dfs(n):
#     visited[n] = 1
#     for w in arr[n]:
#         if visited[w] == 0:
#             visited[w] = 1
#             dfs(w)

# res = 0
# for i in range(1,N+1):
#     if visited[i] == 0:
#         dfs(i)
#         res += 1
# print(res)