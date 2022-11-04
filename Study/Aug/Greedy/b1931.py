N = int(input())
greeting = [tuple(map(int,input().split())) for _ in range(N)]

def getkey(g):
    return g[1]

def getkey_0(g):
    return g[0]

greeting.sort(key=getkey_0)
greeting.sort(key=getkey)

result = i = 0

for s,e in greeting:
    if s >= i:
        result += 1
        i = e

print(result)

# while문 대신 for문 작성 (3,7), (4,5), (5,6) 처럼 greeting[N-1][1] 가기전까지 회의실 배정이 끝나면 i가 무한 증가하므로 인덱스 에러
# - 2프로 or 5프로 런타임 에러
# def getkey(g):
#     return g[1]
# 
# def getkey_0(g):
#     return g[0]
# 
# greeting.sort(key=getkey_0)
# greeting.sort(key=getkey)
# 
# result = i = 0
# min_e = 0
# 
# while min_e < greeting[N-1][1]:
#     if min_e <= greeting[i][0]:
#         result += 1
#         min_e = greeting[i][1]
#     i += 1
# 
# print(result)


## 1
# min_e = greeting[0][1]
# last_e = greeting[N-1][1]
#
# while True:
#     if min_e == last_e:
#         break
#     else:
#         if min_e <= greeting[i][0]:
#             result += 1
#             min_e = greeting[i][1]
#         i += 1
#
# print(result)




# - 선택 정렬 = 시간초과
# for i in range(N):
#     min_e = i
#     for j in range(i+1,N):
#         if greeting[min_e][1] > greeting[j][1]:         # 오름차순 정렬
#             min_e = j
#     greeting[min_e], greeting[i] = greeting[i], greeting[min_e]
#
# max_e = greeting[N-1][1]
# time = [0] * (max_e+1)
# result = 0
#
# for i in range(N):
#     cnt = 0
#     s, e = greeting[i][0], greeting[i][1]
#     for c in range(s,e+1):
#         cnt += time[c]
#     if cnt == 0:
#         result += 1
#         for t in range(s+1,e):
#             time[t] = 1