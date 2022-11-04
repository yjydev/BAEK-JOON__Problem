# 두 수 비교하기
A,B = list(map(int,input().split(' ')))
print('>' if A > B else ('<' if A < B else '=='))