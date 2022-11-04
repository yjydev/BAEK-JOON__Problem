def check(Lo):
    if len(L) == 6:
        print(' '.join(map(str,L)))
        return
    else:
        for i in range(len(Lo)):
            L.append(Lo[i])
            check(Lo[i+1:])
            L.pop(-1)

while True:
    li = list(map(int,input().split()))
    k = li[0]
    if k == 0:
        break
    else:
        num = li[1:]
        L = []
        check(num)
    print()





