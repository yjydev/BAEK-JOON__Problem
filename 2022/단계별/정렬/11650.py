#좌표 정렬하기
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
board.sort(key=lambda x: (x[0],x[1]))  # key 가 여러개일 경우 튜플로 작성 가능 => 정렬 기준 순서대로
# (x[0], x[1]) 으로 작성하면, x[0] 원소를 기준으로 정렬하고 + 같으면 x[1] 기준으로 정렬한다는 듯
for i in range(N):
    print(' '.join(list(map(str,board[i]))))
# 다른 모듈 import 없이 2중 리스트를 펼치기 위해 for문 활용