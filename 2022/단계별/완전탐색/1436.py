#영화감독 숌
N = int(input())
num = 666
cnt = 0
# 끝 범위를 모르니까 for문이 아닌 while 문으로 완전탐색 돌리기
while True:
    if cnt == N :
        print(num-1)
        break
    if str(num).count('666'):
        cnt += 1
    num += 1
