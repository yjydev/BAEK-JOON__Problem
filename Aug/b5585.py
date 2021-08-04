n = 1000 - int(input())
cnt = 0
if n >= 500:
    cnt += 1
    n -= 500
for i in [100, 50, 10, 5, 1] :
    cnt += n // i
    n = n % i

print(cnt)