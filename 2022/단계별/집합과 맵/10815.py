# 숫자 카드

N = int(input())
cards = list(map(int,input().split()))
M = int(input())
check_list = list(map(int,input().split()))
# check_list의 각 숫자 카드 중에서, cards에 포함되어 있으면 1, 아니면 0 출력
# => 즉, check_list엔 있지만 cards에 없으면 0, 둘 다 있으면 1인 것이므로
# => check_list - cards 차집합을 구해서 그 원소들만 0을 출력하면 된다.
diff = set(check_list)-set(cards)
for check in check_list:
    if check in diff:
        print(0, end = ' ')
    else:
        print(1, end = ' ')
