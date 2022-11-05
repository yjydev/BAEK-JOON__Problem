#최댓값
res = [0,0]
for i in range(1,10):
    n = int(input())
    if res[0] < n:
        res[0] = n
        res[1] = i
print(res[0])
print(res[1])