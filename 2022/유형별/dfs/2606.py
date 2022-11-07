#바이러스
N,V = int(input()), int(input())
arr = [[] for _ in range(N+1)]
for _ in range(V):
    i,j = map(int,input().split())
    arr[i].append(j)
    arr[j].append(i)
visited = [0] * (N+1)

cnt = 0
def dfs(n):
    global cnt
    visited[n] = 1
    for w in arr[n]:
        if visited[w] == 0:
            cnt += 1
            visited[w] = 1
            dfs(w)
dfs(1)
print(cnt)

# def bfs(n):
#     visited[n] = 1
#     q = [n]
#     cnt = 0
#     while q:
#         i = q.pop()
#         for w in arr[i]:
#             if visited[w] == 0:
#                 cnt += 1
#                 visited[w] = 1
#                 q.append(w)
#     return cnt

# print(bfs(1))


