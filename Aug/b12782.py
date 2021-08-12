T = int(input())
for tc in range(1,T+1):
    N,M = map(str, input().split())
    dif_N = []
    dif_M = []
    cnt = 0
    for i in range(len(N)):
        if N[i] == M[i]:
            continue
        else :
            dif_N.append(N[i])
            dif_M.append(M[i])
    N_0, N_1 = dif_N.count('0'), dif_N.count('1')
    M_0, M_1 = dif_M.count('0'), dif_M.count('1')
    if N_0 == M_1 and N_1 == M_0 :
        if N_0 < N_1:
            cnt += N_1
            # N_0 + (N_1 - N_0) 이라서
            # 둘 중 적은 횟수만큼 교환 + 교환횟수 뺀만큼 0,1 교체횟수 
        else :
            cnt += N_0
    else:
        cnt += N_0 + N_1
    print(cnt)


