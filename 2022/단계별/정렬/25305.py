# 커트라인
N, k = map(int,input().split())
li = sorted(list(map(int,input().split())), reverse=True)
print(li[k-1])   # 리스트 인덱스는 0부터 시작이므로 -1
