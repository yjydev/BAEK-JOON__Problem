# 대표값2
N = 5    # 일반화 목적
li = sorted([int(input()) for _ in range(N)])
print(sum(li)//N)
print(li[(N-1)//2])