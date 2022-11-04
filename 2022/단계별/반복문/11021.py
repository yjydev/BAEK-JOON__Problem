T = int(input())
for t in range(1,T+1):
    res = sum(list(map(int,input().split( ))))
    print(f'Case #{t}: {res}')
