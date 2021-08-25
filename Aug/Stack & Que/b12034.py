T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    li_1 = []
    stack = []
    result = []
    while li:
        t = li.pop(0)
        if not t % 4:
            stack.append(t)     # 정상가 후보들
        else:
            li_1.append(t)      # 할인가격 일부

    while stack:
        k = stack.pop()         # 정상가 후보 중 하나를 뒤부터 빼서 k에 저장 - 그래야 stack에 들어온 후보가격이 있다면 탐색할 수 있으므로
        m = int(k*0.75)         # k의 할인가격
        if m in li_1:       # k의 할인가격이 할인가격 리스트안에 있다면
            result.append(m)
            li_1.remove(m)
        elif m in stack:
            result.append(m)       # 정상가 후보 리스트에 있다면, 후보가격이 4의 배수라서 정상가 후보로 포함되었던 것
            stack.remove(m)
    print('Case #{}: {}'.format(tc, ' '.join(map(str,result[-1::-1]))))
    
