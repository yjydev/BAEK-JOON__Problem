# 원하는 원판 나올때까지 2로 옮겨두고 원하는 원판만 3으로 옮기기 
# -> 1 탐색 끝나면 2탐색 -> 2탐색 끝나면 1탐색 (3에 N개가 다 찰 때까지 반복)
N = int(input())
target = N
stack_1 = list(map(int,input().split()))
stack_2 = []
stack_3 = []
result = []
while len(stack_3) < N:
    while stack_1:
        k = stack_1.pop()
        if k == target:               # 현재 가장 큰 원판
            stack_3.append(k)
            result.append('1 3')
            target -= 1
        else:
            stack_2.append(k)
            result.append('1 2')
    else:
        while stack_2:
            k_2 = stack_2.pop()
            if k_2 == target:
                stack_3.append(k_2)
                result.append('2 3')
                target -= 1
            else:
                stack_1.append(k_2)
                result.append('2 1')
print('{}'.format(len(result)))
print('{}'.format('\n'.join(map(str, result))))