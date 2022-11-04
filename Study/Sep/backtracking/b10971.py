# min_cost 가 작은 값이라서 계속 틀렸었던 거였다..
# + 순열로 가능한 경우의 수 완전탐색하지 말고 재귀로 탐색하며 가지치기해줬어야 하는것

import sys

N = int(sys.stdin.readline())
W = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
min_cost = 999999999

def check(start, cost, last):
    global min_cost
    if min_cost < cost + W[start][last]:        # 최소값보다 현재 위치에서 마지막 위치로 돌아가는 비용이 더 크다면 불가능하므로 가지치기
        return

    if (sum(visited) == N) and W[start][last]:  # 도시를 모두 방문하고 + 다시 돌아오는 경우가 존재한다면
        cost += W[start][last]
        if min_cost > cost:
            min_cost = cost
        return
    else:
        for j in range(N):
            if W[start][j] and visited[j] == 0:
                visited[j] = 1
                check(j, cost+W[start][j], last)
                visited[j] = 0

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    check(i, 0, i)  # 결국 처음 출발한 도시로 다시 돌아와야하므로 start = last = i 로 동일
print(min_cost)



# 그냥 이중포문 돌리다보니 1 -> 2, 1-> 3 이런식으로 순회가 아닌 그냥 반복일 뿐이라 다시 생각해서
# bfs 하려다가 생각해보니 순회 도는 경우의 수를 구하면 되는거니가 이번에도 순열을 구해보면..? -> 시간초과


# 오답
# arrList = [[] for _ in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         if W[i][j] != 0:
#             arrList[i].append(j)

# def check(N, cost, last):
#     global min_cost
#     if sum(visited) == N:
#         cost += W[last][0]
#         if min_cost > cost:
#             min_cost = cost
#         return
#     else:
#         for i in arrList[]
#                 if (i != j) and visited[j] == 0:
#                     cost = cost + W[i][j]
#                     visited[i] = 1
#                     visited[j] = 1
#                     check(N, cost, j)
#                     visited[j] = 0
#                     cost -= W[i][j]

# 메모리 초과
# N = int(input())
# W = [list(map(int,input().split())) for _ in range(N)]
# min_cost = 99999
# result = []
#
# def per(i, n):
#     if i == n:
#         result.append(L[:])
#     else:
#         for j in range(i,n):
#             L[i],L[j] = L[j], L[i]
#             per(i+1,n)
#             L[i], L[j] = L[j], L[i]
#
# L = list(range(N))
# per(0,N)
# for res in result:
#     cost = last = 0
#     for i in range(N-1):
#         if W[res[i]][res[i+1]] != 0:
#             cost += W[res[i]][res[i+1]]
#         else:
#             break
#     if W[res[-1]][res[0]] != 0:
#         cost += W[res[-1]][res[0]]
#         if min_cost > cost:
#             min_cost = cost
#
# print(min_cost)

# 10% 시간초과
# from itertools import permutations
# import sys
#
# N = int(sys.stdin.readline())
# W = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# min_cost = 99999
#
# L = list(range(N))
# result = permutations(L)
# flag = True
#
#
# for res in result:
#     cost = last = 0
#     for i in range(N-1):
#         if W[res[i]][res[i+1]] != 0:
#             cost += W[res[i]][res[i+1]]
#         else:
#             flag = False
#             break
#     if (flag is True) and (W[res[-1]][res[0]] != 0):
#         cost += W[res[-1]][res[0]]
#         if min_cost > cost:
#             min_cost = cost
#
# print(min_cost)