N = int(input())
YN = [list(input()) for _ in range(N)]
check = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if j != k:
                if YN[j][k] == 'Y' or (YN[j][i] == 'Y' and YN[k][i] == 'Y'):    # j와 k가 친구 / (j와 친구인 i, k와 친구인 i 가 존재) -> j와 k도 2-친구
                    check[j][k] = 1

result = 0
for i in check:
    result = max(result, sum(i))    # sum(i) 는 i의 친구수 총합 (i가 [0,1,1]이면 b,c와 친구라는 뜻 = 2명)
print(result)


# dfs 시도..
# for i in range(N):
#     for j in range(N):
#         if YN[i][j] == 'Y':                 # YN 리스트는 인덱스 0번부터, arrList는 인덱스 1번부터 시작이므로
#             arrList[i+1].append(j+1)        # YN 리스트 자체가 1,2 랑 2,1 모두 포함하므로 한 번에 한 쪽만 추가해도 ok
# def dfs():
#     global N
#     result = 0
#     for k in range(1, N+1):               # 인접이 있든말든 모조리 순회돌면 인접없는 곳은 인덱스 에러날지도..?
#         visited = [0 for _ in range(N+1)]
#         visited[k] = 1
#         cnt = 0
#         for w in arrList[k]:
#             if visited[w] == 0:
#                 cnt += 1
#                 visited[w] = 1
#                 for v in arrList[w]:
#                     if visited[v] == 0:
#                         cnt += 1
#                         visited[v] = 1
#         if result < cnt:
#             result = cnt
#     return result
# print(dfs(1))

#
# def dfs(k):
#     l = arrList
#     global N
#     q = []
#     q.append(k)
#     visited = [0] * (N+1)
#     while q:
#         t = q.pop(0)
#         for w in arrList[t]:
#             visited[w] += 1
#             for v in arrList[w]:
#                 visited[v] += 1
#                 if t != v:
#                     q.append(v)
#
#     return max(visited)



# def dfs(n):
#     stack = []
#     i = n
#     visited[i] = 1
#     while True:
#         cnt = 0
#         for w in arrList[i]:
#             if visited[w] == 0:
#                 stack.append(i)
#                 i = w
#                 visited[w] = 1
#                 cnt += 1
#         else:
#             if stack:
#                 i = stack.pop()
#             else:
#                 break