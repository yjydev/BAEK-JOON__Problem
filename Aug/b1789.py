N = int(input())
res = 0
cnt = 0
for i in range(1,N+2):
    res += i
    cnt += 1
    if N < res:
        cnt-=1
        break
print(cnt)

# N = int(input())
# a = 1
# while (a * (a+1))/2 <= N :
#     a +=1
# print(a-1)

# N = int(input())
# res = 0
# li=[]
# for i in range(1,N+1):
#     res += i
#     li.append(i)
#     if N < res:
#         break
# print(len(li)-1)

# N = int(input())
# res = 0
# li=[]
# for i in range(1,N+1):
#     res += i
#     li.append(i)
#     if N < res:
#         li.pop(-1)
#         break
# print(len(li))