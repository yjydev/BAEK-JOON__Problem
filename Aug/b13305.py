N = int(input())
lenth = list(map(int,input().split()))
won = list(map(int,input().split()))
cost = 0
for i in range(N-1):       # 마지막은 고려할 필요 없으니까
    if won[i] < won[i+1]:
        won[i+1] = won[i]
    cost += won[i] * lenth[i]
print(cost)


# 41점 (아마 시간복잡도 때문)
# N = int(input())
# lenth = list(map(int,input().split()))
# won = list(map(int,input().split()))
# cost = 0
# for i in range(N-1):
#     for j in range(i,N):
#         if won[i] < won[j]:
#             won[j] = won[i]
#     cost += won[i] * lenth[i]
# print(cost)

# 41점 (아마 시간복잡도 때문22 - for문 하나 차이나는데도 같다.)
# N = int(input())
# lenth = list(map(int,input().split()))
# won = list(map(int,input().split()))
# cost = 0
# for i in range(N):
#     for j in range(i,N):
#         if won[i] < won[j]:
#             won[j] = won[i]
# for k in range(N-1):
#     cost += won[k] * lenth[k]
# print(cost)
