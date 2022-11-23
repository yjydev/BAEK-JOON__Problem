#좌표 정렬하기2
N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
li.sort(key=lambda x : (x[1],x[0]))  # y 좌표 증가 => 같으면 x 좌표 증가 순으로 정렬
for i in li:
    print(i[0],i[1])