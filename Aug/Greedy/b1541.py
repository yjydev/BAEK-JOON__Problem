li = input().split('-')
num = []
for i in li:
    li_1 = i.split('+')
    cnt = 0
    for j in li_1:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for k in range(1,len(num)):
    n -= num[k]
print(n)






