# 교재 스택2 52쪽 공부하기(8/23 강의 다시보기)

N = int(input())
A = list(map(int,input().split()))
result = []


def per(i, n):
    if i == n:
        result.append(L[:])
    else:
        for j in range(i,n):
            L[i], L[j] = L[j], L[i]
            per(i+1,n)
            L[i],L[j] = L[j],L[i]

L = A.copy()
per(0,len(L))

res = 0
for k in range(len(result)):
    ans = 0
    for i in range(N-1):
        ans += abs(result[k][i]-result[k][i+1])
    res = max(ans,res)
print(res)





# 시간초과

# def check(num):             # 배열 A를 나열하는 모든 경우의 수
#     if len(num) == 1:
#         return [num]
#     else:
#         result = []
#         for i in num:
#             L = num[:]
#             L.remove(i)
#             L.sort()
#             for j in check(L):
#                 j.insert(0,i)
#                 if j not in result:
#                     result.append(j)
#         return result
#
#
# nums = check(A)
# res = 0
# for k in range(len(nums)):
#     ans = 0
#     for i in range(N-1):
#         ans += abs(nums[k][i]-nums[k][i+1])
#     res = max(ans,res)
# print(res)