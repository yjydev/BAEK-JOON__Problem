#보물
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
while A:
    a = min(A)
    b = max(B)
    ans += a*b
    A.remove(a)
    B.remove(b)
print(ans)
