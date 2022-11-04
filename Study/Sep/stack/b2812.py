N,K = map(int,input().split())
number = list(map(int,input()))
stack = []
cnt = K

for i in range(N):
    while stack and (number[i] > stack[-1]) and cnt:
        stack.pop()
        cnt -= 1
    stack.append(number[i])
print(''.join(map(str,stack[:N-K])))













# pop하는게 아니라 주호님처럼 front, tail 하나씩 늘리는 방식으로 풀 수 있을듯..?
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
