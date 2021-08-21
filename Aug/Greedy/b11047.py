N, K = map(int, input().split())
li = []
cnt = 0
for i in range(N):
    li.insert(0, int(input()))
for j in li:
    cnt += K//j
    K %= j
print(cnt)

