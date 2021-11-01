
N, S = map(int,input().split())
nums = list(map(int,input().split()))
res = 0

for i in range(1, 1<<N):
    sub = []
    for j in range(N):
        if i & (1<<j):
            sub.append(nums[j])
    if sum(sub) == S:
        res += 1
print(res)
