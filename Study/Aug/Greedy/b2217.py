N = int(input())
li = [int(input()) for _ in range(N)]
w = []
li.sort()
for i in range(N):
    w.append(li[i] * (N-i))
print(max(w))

# 10 20 30 이라고 할때, 
# 10* N , 20 * N , 30 * N 중 최소값이 로프 셋 다 감당가능한 중량이므로 10 *N
# 로프 갯수를 줄일 수도 있으니 20 * N-1 , 30 * N-1 중 최소. 즉, 20 * N-1
# 이렇게 하면 10 * N, 20 * N-1, 30 * N-2 가 감당 가능한 중량인 것
# 결론은 li 정렬한 후, li[0] * N, li[1] * N-1 ... 이 가능한 중량들이니 그 중 최대 찾으면 되는것

# 내장함수 x - 시간초과
# N = int(input())
# li = [int(input()) for _ in range(N)]
# for i in range(N-1, -1, -1):
#     for j in range(i):
#         if li[j] > li[j+1]:
#             li[j] , li[j+1] = li[j+1] , li[j]
# w = li[0] * N
# for i in range(1,N):
#     if w < li[i] * (N-i):
#         w = li[i] * (N-i)
# print(w)
