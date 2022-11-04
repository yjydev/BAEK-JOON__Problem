#더하기 사이클
N = int(input())
cur = N
cnt = 0
while True:
    sum_val = (cur//10) + (cur%10)
    cur= (cur%10) * 10 + (sum_val % 10)
    cnt += 1
    if N == cur:
        break
print(cnt)