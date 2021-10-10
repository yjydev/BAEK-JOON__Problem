
# input() 으로 쓰면 pypy로만 통과
# sys.stdin.readline() 로 쓰면 python3 으로도 통과

N, Q = map(int,input().split())
land = [int(input()) for _ in range(Q)]
parent = [[] for _ in range(Q)]
visited = [0] * (N+1)
for i in range(Q):
    flag = True
    l = land[i]
    while l :
        if l % 2 == 0:
            parent[i].append(l)
            l //= 2
        if l % 2:
            parent[i].append(l)
            l = (l-1)//2
    parent[i] = parent[i][::-1]
    for k in range(len(parent[i])):
        m = parent[i][k]
        if visited[m] == 1:
            print(m)
            flag= False
            break
    if flag is True:
        visited[land[i]] = 1
        print(0)





# 시간 초과
# N, Q = map(int,input().split())
# land = [int(input()) for _ in range(Q)]
# tree = [[] for _ in range(N+1)]
# li = [i for i in range(N+1)]
#
# for k in range(1,(N+1)//2+1):
#     p = li[k]
#     if N >= k*2:
#         tree[p].append(li[k*2])
#     if N >= k*2+1:
#         tree[p].append(li[k*2+1])
# visited = [0] * (N+1)
# j = -1
# while j < len(land)-1:
#     m = 1
#     flag = True
#     parent = []
#     j += 1
#     t = land[j]
#     while m < len(tree):
#         if t in tree[m]:
#             parent.append(m)
#             t = m
#             m = 0
#         else:
#             m += 1
#     for v in parent:
#         if visited[v] == 1:
#             print(v)
#             flag = False
#             break
#     if flag is True:
#         visited[land[j]] = 1
#         print(0)





