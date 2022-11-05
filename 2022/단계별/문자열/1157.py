#단어 공부
S = input().lower()
fre = list(map(lambda x: S.count(chr(x)), range(97,123)))
fre_cnt = max(fre)
if fre.count(fre_cnt) > 1:
    print('?')
else:
    print(chr(65+fre.index(fre_cnt)))

# 함수를 따로 변수에 저장해두고 나중에 활용하는 것도 가능
# c = S.count
# fre = list(map(lambda x: c(chr(x)), range(97,123)))

# 입력받은 알파벳들 범위내로도 해결 가능
# S = input().upper()
# fre = [0,'']
# for s in set(S):
#     cnt = S.count(s)
#     if fre[0] == cnt:
#         fre[1] = '?'
#     if fre[0] < cnt:
#         fre[0] = cnt
#         fre[1] = s
# print(fre[1])
