def find(start,arr):
    global cnt
    visited[start] = 1
    for a in arr[start]:
        if visited[a] == 0:
            cnt += 1
            find(a,arr)

N,M = map(int,input().split())
heavy = [[] for _ in range(N+1)]
light = [[] for _ in range(N+1)]
res = 0

for _ in range(M):
    a,b = map(int,input().split())
    heavy[b].append(a)
    light[a].append(b)

for i in range(1,N+1):
    visited = [0] * (N + 1)
    cnt = 0
    find(i,heavy)
    if cnt >= (N+1)//2 :
        res += 1
    else:
        cnt = 0
        visited = [0] * (N+1)
        find(i,light)
        if cnt >= (N+1)//2:
            res += 1
print(res)

# N,M = map(int,input().split())
# heavy = [0]*(N+1)
# light = [0]*(N+1)
# res = 0
#
# for _ in range(M):
#     a,b = map(int,input().split())
#     heavy[a] += 1
#     light[b] += 1
#
# for i in range(1,N+1):
#     if heavy[i] >= N//2 or light[i] >= N//2:
#         res += 1
# print(res)


# 5 > 3 > 1 인경우, 5보다 가벼운게 3밖에 안잡힘... 1도 찾아야하므로 더 들어가서 깊게 dfs 재귀 활용해야함
# def find(start,arr,cnt):
#     global res
#     visited[start] = 1
#     for a in arr[start]:
#         if visited[a] == 0:
#             cnt += 1
#             visited[a] = 1
#     if cnt >= N//2:
#         res += 1
#         return True
#     return False
#
# N,M = map(int,input().split())
# heavy = [[] for _ in range(N+1)]
# light = [[] for _ in range(N+1)]
# res = 0
#
# for _ in range(M):
#     a,b = map(int,input().split())
#     heavy[b].append(a)
#     light[a].append(b)
#
# for i in range(1,N+1):
#     visited = [0] * (N + 1)
#     if find(i,heavy,0) is False :
#         visited = [0] * (N + 1)
#         find(i,light,0)
#
# print(res)




