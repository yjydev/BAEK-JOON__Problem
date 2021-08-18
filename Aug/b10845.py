import sys

N = int(sys.stdin.readline())
que = []
for k in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        que.append(order[1])
    if order[0] == 'pop' :
        if que:
            print(que.pop(0))
        else:
            print(-1)
    if order[0] == 'size':
        print(len(que))
    if order[0] == 'empty':
        if que :
            print(0)
        else:
            print(1)
    if order[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    if order[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)

    
