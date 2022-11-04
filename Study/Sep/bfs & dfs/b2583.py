# 정답1. 함수 없이 풀기
M,N,K = map(int, input().split())
board = [[0]*N for _ in range(M)]
for _ in range(K):
    sx,sy,ex,ey = map(int,input().split())
    for i in range(sy,ey):
        for j in range(sx,ex):
            board[i][j] = 1             # 직사각형 그려진 부분을 1로 채우기

arrList = [[[] for _ in range(N)] for _ in range(M)]
di=[1,-1,0,0]
dj=[0,0,1,-1]
for i in range(M):
    for j in range(N):
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0 <= ni < M and 0 <= nj < N:
                if board[ni][nj] == 0:
                    arrList[i][j].append([ni,nj])   # i,j에서 갈 수 있는 곳들 인접리스트 추가
result = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:          # board 값이 0인 좌표에 대해서 bfs 탐색
            cnt = 1
            board[i][j] = 1
            q = [[i,j]]
            while q:
                t = q.pop(0)
                t1,t2 = t[0], t[1]
                for w in arrList[t1][t2]:
                    w1,w2 = w[0], w[1]
                    if board[w1][w2] == 0:      # 좌표가 0이면, 갈 수 있는 곳이므로 1로 바꾸고 cnt 1추가(=영역 넓이 1추가)
                        q.append(w)
                        board[w1][w2] = 1
                        cnt += 1
            result.append(cnt)          # while문 한번 끝날때마다(=더이상 인접이 없는=갈 수 있는 곳이없으면) 영역 하나 탐색 끝난 것 / 결과 저장
result.sort()                           # 넓이는 오름차순 정렬하라고 했으므로 sort
print(len(result))                      # 저장된 넓이의 개수가 영역 개수
print(' '.join(map(str,result)))



# 정답 2. 함수로 풀기
# bfs 돌면서 갈수있는 곳 없으면 그때까지의 넓이 저장 -> 저장된 넓이의 개수 = 영역갯수

# M, N, K = map(int, input().split())
# board = [[0] * N for _ in range(M)]
# for _ in range(K):
#     sx, sy, ex, ey = map(int, input().split())
#     for i in range(sy, ey):
#         for j in range(sx, ex):
#             board[i][j] = 1
# arrList = [[[] for _ in range(N)] for _ in range(M)]
# di = [1, -1, 0, 0]
# dj = [0, 0, 1, -1]
# visited = [[0] * (N + 1) for _ in range(M)]
# for i in range(M):
#     for j in range(N):
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < M and 0 <= nj < N:
#                 if board[ni][nj] == 0:
#                     arrList[i][j].append([ni, nj])
#
#
# def bfs(n):
#     cnt = 1
#     q = []
#     q.append(n)
#     n1, n2 = n[0], n[1]
#     board[n1][n2] = 1
#     while q:
#         t = q.pop(0)
#         t1, t2 = t[0], t[1]
#         for w in arrList[t1][t2]:
#             w1, w2 = w[0], w[1]
#             if board[w1][w2] == 0:
#                 q.append(w)
#                 board[w1][w2] = 1
#                 cnt += 1
#     result.append(cnt)
#
#
# result = []
# for i in range(M):
#     for j in range(N):
#         if board[i][j] == 0:
#             bfs([i, j])
#
# result.sort()
# print(len(result))
# print(' '.join(map(str, result)))

