#좌표 압축
#좌표 압축 = 해당 원소보다 작은 수의 개수
# 즉, 오름차순 정렬했을 때의 (중복 제외) 인덱스 값이나 다름없다.
# 2 4 -10 4 -9 의 경우엔 정렬하면 -10 -9 2 4 4 인데 
# -10보다 작은건 0개, -9보다 작은건 1개 등 인덱스와 동일하다.
N = int(input())
board = list(map(int,input().split()))
# 중복 제외이므로 set / board는 출력할 때 필요하므로 배열 복사
tmp = list(set(board[:]))   
tmp.sort()
# 딕셔너리를 만드는데, 값을 key, 인덱스를 value 로 만든다.
li = {tmp[i] : i for i in range(len(tmp))}
for b in board:
    # 각 값에 대한 인덱스를 딕셔너리에서 꺼내와서 출력하면 된다.
    print(li[b], end=' ')
    # list[i] => 시간 복잡도 O(1)

# 시간초과
# for b in board:
#     print(tmp.index(b), end=' ')
    # .index(n) => 시간 복잡도 O(N)