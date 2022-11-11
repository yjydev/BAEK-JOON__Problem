# 통계학
# 최빈값 구할 때 Collections 모듈의 Counter 없이 내장함수인 count를 쓰니까 시간초과 발생
import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
li = sorted([int(input()) for _ in range(N)])
print(round(sum(li)/N))
print(li[(N-1)//2])  # N이 홀수이므로
cnt = Counter(li).most_common()
m = cnt[0][1]
l = list(filter(lambda x: x[1] == m, cnt))
if len(l) == 1:
    print(l[0][0])
else:
    print(l[1][0])
print(max(li)-min(li))

# 최빈값 내장 함수 - 시간 초과
# s = set(li)
# cnt = list(map(lambda x : li.count(x), s))
# m = []
# for i in range(len(s)):
#     if cnt[i] == max(cnt):
#         m.append(list(s)[i])
# if len(m) > 1:
#     m.remove(min(m))
# print(min(m))
