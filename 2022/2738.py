# 행렬 덧셈    

N,M = list(map(int,input().split(' ')))
A = [list(map(int,input().split(' '))) for i in range(N)]
B = [list(map(int,input().split(' '))) for i in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]
for a in A:
    print(*a)
    

# 처음 풀이   

# N,M = list(map(int,input().split(' ')))
# A = [list(map(int,input().split(' '))) for i in range(N)]
# B = [list(map(int,input().split(' '))) for i in range(N)]
# for i in range(N):
#     for j in range(M):
#         print(A[i][j] + B[i][j], end=' ')
#     print()

