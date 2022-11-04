A,B = map(int,input().split())
L, R = 0,0

def check(a,b):
    global L, R
    if a ==1 and b==1:
        return
    if a == 1:
        R += b-1
        return
    if b == 1:
        L += a-1
        return
    if a < b:
        R += b//a
        check(a, b%a)
    if a>b:
        L += a//b
        check(a%b, b)

check(A,B)
print('{} {}'.format(L,R))

