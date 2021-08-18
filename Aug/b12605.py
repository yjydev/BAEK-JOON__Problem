N = int(input())
stack = []
for tc in range(1,N+1):
    stack = input().split()
    top = len(stack)-1
    result = [stack[i] for i in range(top,-1,-1)]
    print('Case #{}: {}'.format(tc, ' '.join(result)))


# pop 함수 정의 
N = int(input())
stack = []

def pop():
    global top
    top -= 1
    return stack[top+1]

for tc in range(1,N+1):
    stack = input().split()
    top = len(stack)-1
    result = [pop() for _ in range(top+1)]
    print('Case #{}: {}'.format(tc, ' '.join(map(str, result))))

