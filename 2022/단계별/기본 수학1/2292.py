#벌집
N = int(input())
cnt, binary = 0, 1
# 방 개수별 범위를 따져서 경계를 기준으로 수열 구성
# 방 1개(1) => 1, 2개(2~7) => 7, 3개(8~19) => 19, ... 
while True:
    if N <= binary:
        break
    cnt += 1
    binary += 6*cnt
print(cnt+1)

# 첫 아이디어 - 일직선으로 가는 수열 생각
# for i in range(2,8):
#     diff = i-1
#     n, cnt = 1, 0
#     while n <= N:
#         if n == N:
#             break
#         n += diff
#         diff += 6
#         cnt += 1
#     print(cnt)