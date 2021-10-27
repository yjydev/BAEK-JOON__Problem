import sys
def dfs(n):
    cnt = 1
    visited = [0] * (N+1)
    stack = []
    stack.append(n)
    visited[n] = 1
    while stack:
        for w in arr[stack[-1]]:
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1
                cnt += 1
                break
        else:
            stack.pop()
    return cnt

N,M = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[b].append(a)
ans = 0
idx = []
for i in range(1,N+1):
    cnt = dfs(i)
    if ans < cnt:
        idx.clear()
        ans = cnt
        idx.append(i)
    elif ans == cnt:
        idx.append(i)
print(*idx)


# 통과 코드...왜?????

# import sys
# def dfs(n):
#     global cnt,N
#     p = n
#     visited = [0] * (N+1)
#     stack = []
#     stack.append(p)
#     visited[p] = 1
#     while stack:
#         p = stack.pop()
#         for w in arr[p]:
#             if visited[w] == 0:
#                 stack.append(w)
#                 visited[w] = 1
#                 cnt += 1
#
# N,M = map(int,sys.stdin.readline().split())
# arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     a,b = map(int,sys.stdin.readline().split())
#     arr[b].append(a)
# ans = 0
# idx = []
# for i in range(1,N+1):
#     cnt = 1
#     dfs(i)
#     if ans < cnt:
#         idx.clear()
#         ans = cnt
#         idx.append(i)
#     elif ans == cnt:
#         idx.append(i)
# print(*idx)



# 재귀 dfs - 시간초과
# import sys
# def dfs(n,cnt):
#     global res
#     for w in arr[n]:
#         if visited[w] == 0:
#             visited[w] = 1
#             cnt += 1
#             dfs(w,cnt)
#             visited[w] = 0
#     res = max(res,cnt)
#
# N,M = map(int,sys.stdin.readline().split())
# arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     a,b = map(int,sys.stdin.readline().split())
#     arr[b].append(a)
#
# ans = 0
# idx = []
# for i in range(1,N+1):
#     visited = [0] * (N + 1)
#     res = 0
#     dfs(i,0)
#     if ans < res:
#         idx.clear()
#         ans = res
#         idx.append(i)
#     elif ans == res:
#         idx.append(i)
# print(*idx)
