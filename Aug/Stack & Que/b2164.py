import collections
N = int(input())
stack = collections.deque(range(1,N+1))
while len(stack) > 1 :
    stack.popleft()
    k = stack.popleft()
    stack.append(k)
print(stack[0])