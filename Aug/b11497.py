T = int(input())
for tc in range(T):
    N = int(input())
    ans = []
    h = list(map(int,input().split()))
    h = sorted(h)[::-1]
    for i in range(N-2):
        ans.append(abs(h[i]-h[i+2]))
        ans.append(h[0]-h[1])
    L = max(ans)
    print(L)    



# 아이디어 - 가장 높은 통나무를 가운데 두고 나머지를 정렬하는 방법
# 차가 최소가 되게 히려면 7 5 3 1 2 4 6 이런식으로 번갈아 둬야 함
 