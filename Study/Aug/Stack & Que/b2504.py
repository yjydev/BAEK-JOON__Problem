import sys
li = list(input())
stack = []
result = ans = 0
for i in li:
    ans = 0
    if i == '(' or i == '[':
        stack.append(i)
    elif stack and i == ')':
        while stack:
            t = stack.pop()
            if t == '[':
                print(0)
                sys.exit()
            elif t == '(':
                if not ans:
                    stack.append(2)
                else:
                    stack.append(ans * 2)
                break
            else:
                ans += int(t)
    elif stack and i == ']':
        while stack:
            t = stack.pop()
            if t == '(':
                print(0)
                sys.exit()
            elif t == '[':
                if not ans:
                    stack.append(3)
                else:
                    stack.append(ans * 3)
                break
            else:
                ans += int(t)
    else:
        print(0)
        sys.exit()
for s in stack:
    if type(s) == int:
        result += s
    else:
        print(0)
        sys.exit()
print(result)





# li = list(input())
# stack = []
# result = []
# ans = 0
#
# def cal(n):
#     global ans
#     if not result:
#         result.append(n)
#     else:
#         if len(result) == 1:
#             if result[-1] == n:
#                 ans = (ans + result.pop()) * n
#             else:
#                 result.append(n)
#         elif result[-1] == n :
#             ans += result.pop() * n
#         else:
#             result.append(n)
#     return ans
#
#
# for i in li:
#     if i == '(' or i == '[':
#         stack.append(i)
#     elif i == ')' or i == ']':
#         if stack[-1] == '(':
#             stack.pop()
#             ans += cal(2)
#         elif stack[-1] == '[':
#             stack.pop()
#             ans += cal(3)
#         else:
#             ans = 0
#             break
# print(ans)




    # if (not result) or (result[-1] != n):
    #     result.append(n)
    # elif len(result) == 1:
    #     if result[-1] == n:
    #         ans = (ans + result.pop()) * n
    #     else:
    #         result.append(n)
    # elif result[-1] == n:
    #     ans += result.pop() * n

