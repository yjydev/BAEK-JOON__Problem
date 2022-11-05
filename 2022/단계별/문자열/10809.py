#알파벳 찾기
S = input()
for i in range(97,123):
    a = chr(i)
    print(S.find(a), end=' ')