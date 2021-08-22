N = int(input())
stack_1 = list(map(int,input().split()))
stack_2 = []
stack_3 = []
result = []
K = len(stack_3)
while K < N :
    if len(stack_1) > 1:
        if stack_1[-1] < stack_1[-2] :
            stack_2.append(stack_1.pop())
            result.append('1 2')
        else:
            stack_3.append(stack_1.pop())
            result.append('1 3')
    elif len(stack_1) == 1:
        if stack_2[-1] < stack_1[0] < stack_3[-1]:
            stack_3.append(stack_1.pop())
            result.append('1 3')
        elif stack_1[0] > stack_2[-1]:
            stack_3.append(stack_2.pop())
            result.append('2 3')
    else :
        if stack_2[-1] < stack_3[-1]:
            stack_3.append(stack_2.pop())
            result.append('2 3')
print(result)

