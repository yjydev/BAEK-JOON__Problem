#덩치
N = int(input())
size = []
res = []
for _ in range(N):
    size.append(list(map(int,input().split())))
for x,y in size:
    cnt = 1
    for nx,ny in size:
        if x < nx and y < ny:
            cnt += 1
    res.append(cnt)
print(*res)

