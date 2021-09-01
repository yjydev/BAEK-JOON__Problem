li = list(input())
stack = []
result = []
ans = 0

def cal(n):
    global ans
    if not result:
        result.append(n)
    else:
        if len(result) == 1:
            if result[-1] == n:
                ans = (ans + result.pop()) * n
            else:
                result.append(n)
        elif result[-1] == n :
            ans += result.pop() * n
        else:
            result.append(n)
    return ans


for i in li:
    if i == '(' or i == '[':
        stack.append(i)
    elif i == ')' or i == ']':
        if stack[-1] == '(':
            stack.pop()
            ans += cal(2)
        elif stack[-1] == '[':
            stack.pop()
            ans += cal(3)
        else:
            ans = 0
            break
print(ans)




    # if (not result) or (result[-1] != n):
    #     result.append(n)
    # elif len(result) == 1:
    #     if result[-1] == n:
    #         ans = (ans + result.pop()) * n
    #     else:
    #         result.append(n)
    # elif result[-1] == n:
    #     ans += result.pop() * n

