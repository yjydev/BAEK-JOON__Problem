#블랙잭
# N장 중 3장 선택, 합이 M 이하이면서 M과 가장 가깝게 만들어야함
# import itertools
# N,M = map(int,input().split())
# cards = list(map(int,input().split()))
# comb = itertools.combinations(cards,3)
# comb_sum = list(map(lambda x : sum(x), comb))
# comb_sum.sort(reverse=True)
# for c in comb_sum:
#     if c <= M:
#         print(c)
#         break

# 조합 없이 구현해보기
N, M = map(int,input().split())
cards = list(map(int,input().split()))
candidate = []
for i in range(len(cards)):
    for j in range(i+1,len(cards)):
        for k in range(j+1, len(cards)):
            s = cards[i] + cards[j] + cards[k]
            if  s <= M:
                candidate.append(s)
            else :
                continue
print(max(candidate))
