N = int(input())
li=[]
if N%10 :
    print(-1)
else:
    for i in [300,60,10]:
        a = N // i
        N %= i
        li.append(a)
    print('{0} {1} {2}'.format(li[0], li[1], li[2]))

# N = int(input())
# li = []
# for i in [300,60,10]:
#     cnt=0
#     cnt += N // i
#     N %= i
#     li.append(cnt)

# if N :
#     print(-1)
# else:
#     print('{0} {1} {2}'.format(li[0], li[1], li[2]))