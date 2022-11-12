#팩토리얼
N = int(input())
res = 1
def fac(n):
    global res
    if n < 2:
        return
    else:
        res *= n
        fac(n-1)
fac(N)
print(res)
