# 뚫고 지나가는 경로와 안뚫고 지나가는 경로가 겹쳐서 방문표시하는게 애매함

import sys

def bfs(n):
    global result
    que = []
    que.append(n)
    visited1[n[0]][n[1]] = 1
    visited2[n[0]][n[1]] = 1
    while que:
        i,j,flag = que.pop(0)
        if i == N and j == M:
            if flag:
                result = visited2[i][j]
            elif flag == 0:
                result = visited1[i][j]
            if visited2[i][j] and visited1[i][j]:
                result = min(visited2[i][j], visited1[i][j])
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni <= N and (0 <= nj <= M):
                if flag == 1 and visited2[ni][nj] == 0:
                    if board[ni][nj] == 0:
                        que.append([ni,nj,flag])
                        visited2[ni][nj] = visited2[i][j] + 1

                elif flag == 0 and visited1[ni][nj] == 0:
                    if board[ni][nj] == 0:
                        que.append([ni,nj,flag])
                        visited1[ni][nj] = visited1[i][j] + 1
                    else:
                        que.append([ni,nj,1])
                        visited2[ni][nj] = visited1[i][j] + 1

    if result == 987654321:
        result = -1

N, M = map(int,sys.stdin.readline().split())
board = [list(map(int,input())) for _ in range(N)]
N -= 1
M -= 1
di = [1,-1,0,0]
dj = [0,0,1,-1]
visited1 =[[0] * (M+1) for _ in range(N+1)]
visited2 = [[0] * (M+1) for _ in range(N+1)]
result = 987654321
bfs([0,0,0])
print(result)



# 반례 통과 못한 코드
# import sys
#
# def bfs(n):
#     global result
#
#     que = []
#     que.append(n)
#     visited[n[0]][n[1]] = 1
#     while que:
#         i,j,flag = que.pop(0)
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni <= N and (0 <= nj <= M) and visited[ni][nj] == 0:
#                 if ni == N and nj == M:
#                     visited[ni][nj] = visited[i][j] + 1
#                     result = min(result,visited[ni][nj])
#                 if board[ni][nj] == 0:
#                     que.append([ni,nj,flag])
#                     visited[ni][nj] = visited[i][j] + 1
#                 elif flag == 0:
#                     que.append([ni,nj,1])
#                     visited[ni][nj] = visited[i][j] + 1
#     if result == 987654321:
#         result = -1
#
# N, M = map(int,sys.stdin.readline().split())
# board = [list(map(int,input())) for _ in range(N)]
# N -= 1
# M -= 1
# di = [1,-1,0,0]
# dj = [0,0,1,-1]
# visited =[[0] * (M+1) for _ in range(N+1)]
# result = 987654321
# bfs([0,0,0])
# print(result)



# 재귀로는 무조건 메모리초과 날수밖에 없는 구조
# import sys
# sys.setrecursionlimit(10**9)
# def bfs(n):
#     global flag, result, flag2
#     i,j = n
#     if visited[i][j] > result:
#         return
#     if n == [N,M]:
#         result = min(result,visited[N][M])
#         flag2 = True
#         return
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0<= ni <= N and (0<= nj <= M) and visited[ni][nj] == 0:
#             if board[ni][nj] == 0:
#                 visited[ni][nj] = visited[i][j] + 1
#                 bfs([ni,nj])
#                 visited[ni][nj] = 0
#             elif flag is True:
#                 flag = False
#                 visited[ni][nj] = visited[i][j] + 1
#                 bfs([ni,nj])
#                 flag = True
#                 visited[ni][nj] = 0
#     return
#
# N , M = map(int,sys.stdin.readline().split())
# board = [list(map(int,input())) for _ in range(N)]
# visited = [[0] * (M+1) for _ in range(N+1)]
# visited[0][0] = 1
# N -= 1
# M -= 1
# flag= True
# flag2 = False
# result = 987654321
# di = [-1,1,0,0]
# dj = [0,0,-1,1]
# # 상 하 좌 우
# result = 987654321
# bfs([0,0])
# if flag2 is False:
#     result = -1
# print(result)

