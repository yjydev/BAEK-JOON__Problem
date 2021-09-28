N,K = map(int,input().split())
number = list(map(int,input()))
stack = []
max_num = num = 0
del_possible = K

for i in range(N):
    while stack and (number[i] > stack[-1]) and del_possible:
        stack.pop()
        del_possible -= 1
    stack.append(number[i])
print(''.join(map(str,stack[:N-K])))














# def check(li, num, i):
#     global max_num, N, K
#     if len(str(num)) == N-K:
#         if num > max_num:
#             max_num = num
#         return
#     else:
#         while stack:
#             a = li.pop()
#             check(li, num+a*(10**i), i+1)
#
#
# l = stack[:]
# check(l, 0, 0)
