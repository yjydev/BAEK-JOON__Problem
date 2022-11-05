#평균은 넘겠지
C = int(input())
for _ in range(C):
    li = list(map(int,input().split( )))
    N = li[0]
    del li[0]
    cnt = len(list(filter(lambda x: x > sum(li)/N, li)))
    print(f'{round(cnt/N*100,3):0.3f}%')