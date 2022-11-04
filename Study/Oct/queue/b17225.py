
A,B,N = map(int,input().split())        # A = 상민포장시각, B = 지수포장시각, N = 손님 수
que = []
ea = 0
eb = 0
for i in range(N):
    t,c,m = input().split()       # t = 주문시각, c = 포장지색, m = 선물 갯수, B = 상민, R = 지수
    t, m = int(t), int(m)
    ea = max(ea,t)
    eb = max(eb,t)
    for k in range(m):
        if c == 'B':
            if t+(ea*k) >= ea:
                que.append([ea, c])
            else:
                que.append([ea,c])
                t = ea
            ea += A

        else:
            if t+(eb*k) > eb:
                que.append([eb,c])
            else:
                que.append([eb,c])
                t = eb
            eb += B
que.sort()
res_1 = []
res_2 = []
num = 1
for q in que:
    if q[1] == 'B':
        res_1.append(num)
        num += 1
    else:
        res_2.append(num)
        num += 1

print(len(res_1))
print(' '.join(map(str,res_1)))
print(len(res_2))
print(' '.join(map(str,res_2)))

#     if c == 'B':
#         for k in range(m):
#             sang[t+A*k].append(1)
#     elif c == 'R':
#         for k in range(m):
#             ji[t+B*k].append(1)
# res_1 = []
# res_2 = []
# num = 1
# for t in range(84600):
#     if sang[t]:
#         for k in range(len(sang[t])):
#             res_1.append(num)
#             num += 1
#     if ji[t]:
#         for k in range(len(ji[t])):
#             res_2.append(num)
#             num += 1








