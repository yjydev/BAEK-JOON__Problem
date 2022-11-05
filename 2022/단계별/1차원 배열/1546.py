#평균
N = int(input())
li = list(map(int,input().split( )))
M = max(li)
n_li = list(map(lambda x: x/M*100, li))
print(sum(n_li)/N)