# 킹, 퀸, 룩, 비숍, 나이트, 폰
standard = [1,1,2,2,2,8]
my = list(map(int,input().split(' ')))
for i in range(6):
    print(standard[i]-my[i], end=' ')