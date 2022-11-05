# X보다 작은 수
N, X = map(int,input().split( ))
A = list(map(int,input().split( )))
for a in A:
    if a < X:
        print(a, end=' ')