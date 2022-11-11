# 수 정렬하기3  
# 내장함수 이용시 메모리초과 (중복 존재 가능) -> 카운팅 정렬(계수 정렬)로 해결 가능
# 주어지는 값이 최대 10,000으로 범위가 작아서 카운팅 정렬해도 ok
import sys
N = int(sys.stdin.readline())
# 개수를 셀 배열 li -> 주어지는 수는 10,000보다 작거나 같으므로 최대 10,001 까지 등장 가능
# index 를 값으로, value 를 개수로 
li = [0] * 10001
for i in range(N):
    # 주어진 숫자 n
    n = int(sys.stdin.readline())
    # n 의 개수 +1
    li[n] += 1
# li를 index로 순회 돌기 -> index 가 출력해야하는 값이니까
# 즉, 0부터 최대값 10,001 까지 순서대로 순회돌기 = 정렬
for l in range(len(li)):
    # l의 개수 = li[l] = cnt 에 담기
    cnt = li[l]
    # l이 존재하면, 즉, cnt != 0 이면 그 개수만큼 출력 (중복이 나올 수도 있으므로)
    if cnt != 0:
        for k in range(cnt):
            print(l)