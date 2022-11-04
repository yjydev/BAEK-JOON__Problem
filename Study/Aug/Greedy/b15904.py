N = input()
ans = ['U','C','P','C']
for i in N:
    if ans :
        if i == ans[0]:
            ans.pop(0)
if not ans:
    print("I love UCPC")
else:
    print("I hate UCPC")
    

# 다른 풀이

# N = input()
# ans = "UCPC"
# j = 0
# for k in range(len(N)):
#     if N[k] == ans[j]:
#         j +=1
#         if j == 4:
#             break

# if j == 4:
#     print("I love UCPC")
# else :
#     print("I hate UCPC")
