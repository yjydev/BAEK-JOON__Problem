N = int(input())
cnt = 0
while N>0:
    if not N % 5:
        cnt += 1
        N -= 5
    else :
        N -= 3
        cnt +=1   
if N < 0:
    print(-1)
else :
    print(cnt)
    

