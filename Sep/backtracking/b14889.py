from itertools import combinations

N = int(input())
S =[list(map(int,input().split())) for _ in range(N)]

num = N // 2            # 한 팀 당 인원

# 팀 정하기
a = []
result = []
min_result = 99999

team = set(range(N))

# 조합으로 가능한 a를 반복으로 돌면서, 각 a에 대해서 최소차이 구하기
for a in combinations(team,num):
    b = list(team - set(a))
    ans_a = ans_b = 0
    for i in range(N // 2):
        for j in range(i+1, N // 2):
            ans_a += S[a[i]][a[j]] + S[a[j]][a[i]]
            ans_b += S[b[i]][b[j]] + S[b[j]][b[i]]
    ans = abs(ans_a - ans_b)
    if min_result > ans:
        min_result = ans

print(min_result)





# 시간초과
# N = int(input())
# S =[([0] + list(map(int,input().split()))) for _ in range(N)]
# S.insert(0,[0]*(N+1))
#
# num = N // 2            # 한 팀 당 인원
# # 팀 정하기
# a = []
# result = []
# min_result = 99999
# team = set(range(N))
#
#
# def check(N):
#     if len(a) == N//2:
#         result.append(a[:])
#         return
#     else:
#         for k in range(N):
#             if k not in a:
#                 a.append(k)
#                 check(N)
#                 a.pop(-1)
#
# check(N)
#
# b = list(team - set(a))
# for a in result:
#     ans = ans_b = 0
#     for i in a:
#         for j in a:
#             if i != j:
#                 ans += S[i][j]
#     for x in b:
#         for y in b:
#             if x != y:
#                 ans_b += S[x][y]
#
#     ans_result = abs(ans-ans_b)
#     if min_result > ans_result:
#         min_result = ans_result
#
# print(min_result)

# import collections
# N = int(input())
# S =[([0] + list(map(int,input().split()))) for _ in range(N)]
# S.insert(0,[0]*(N+1))
# num = N // 2
# a = collections.deque([])
# result = collections.deque([])
# min_result = 99999
# team = set(range(1,N+1))
# def check(N):
#     global min_result
#     if len(a) == N//2:
#         b = list(team - set(a))
#         ans = ans_b = 0
#         for i in a:
#             for j in a:
#                 if i != j:
#                     ans += S[i][j]
#         for x in b:
#             for y in b:
#                 if x != y:
#                     ans_b += S[x][y]
#         ans_result = abs(ans-ans_b)
#         if min_result > ans_result:
#             min_result = ans_result
#         return
#     else:
#         for k in range(1,N+1):
#             if k not in a:
#                 a.append(k)
#                 check(N)
#                 a.pop()
# check(N)
# print(min_result)



