# 함수 정의 x
import sys
N = int(input())
stack = []
for k in range(N):
    stack.append(int(sys.stdin.readline()))
top = len(stack)-1
cnt = 1
a = stack[top]

while top > -1:
    top -= 1
    if a < stack[top]:
        a = stack[top]
        cnt += 1
print(cnt)

# pop 함수 정의
import sys
N = int(input())
stack = []
for k in range(N):
    stack.append(int(sys.stdin.readline()))
top = len(stack)-1
cnt = 1

def pop():
    global top
    top -= 1
    return stack[top+1]

a = pop()
while top > -1:
    k = pop()
    if a < k:
        a = k
        cnt += 1
print(cnt)

