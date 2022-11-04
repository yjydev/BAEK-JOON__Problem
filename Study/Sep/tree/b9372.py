# pypy 로 하면 시간초과 안뜸

def dfs(n,cnt):
    visited[n] = 1
    for w in arrList[n]:
        if visited[w] == 0:
            cnt = dfs(w,cnt+1)
    return cnt


T = int(input())
for tc in range(T):
    N, M = map(int,input().split())     # 국가 N, 비행기 M
    arrList = [[] for _ in range(N+1)]
    for i in range(M):
        n1, n2 = map(int,input().split())
        arrList[n1].append(n2)
        arrList[n2].append(n1)
    visited = [0] * (N + 1)
    cnt = dfs(1,0)
    print(cnt)


# 비행기가 모두 연결되어있으니 최소 비행기 갯수는 N-1

# import sys
#
# T = int(input())
# for tc in range(T):
#     N, M = map(int,input().split())
#     for i in range(M):
#         n1, n2 = map(int,sys.stdin.readline().split())
#     print(N-1)
