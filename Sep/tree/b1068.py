N = int(input())
li = list(map(int,input().split()))
delete = int(input())

def dfs(n, arr):
    li[n] = -2
    for i in range(N):
        if li[i] == n:
            dfs(i,arr)
dfs(delete,li)
ans = 0
for k in range(N):
    if li[k] != -2 and (k not in li):
        ans += 1

print(ans)