N,K = map(int,input().split())
li = list(range(1,N+1))
que = []
j = K-1
while len(li) > 0 :
    if len(li) > 1:
        que.append(li.pop(j))
        j += K-1
        j %= len(li)
    else:
        que.append(li.pop(0))
print('<'+', '.join(map(str,que))+'>')
