#과제 안 내신 분..?
# import sys
# stu = [i for i in range(1,31)]
# submit = [int(sys.stdin.readline()) for _ in range(28)]
# res = set(stu)-set(submit)
# print(min(res))
# print(max(res))
print(*sorted({*range(1,31)}-{int(input()) for _ in range(28)}))