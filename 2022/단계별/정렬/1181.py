#단어 정렬
N = int(input())
li = list(set([input() for _ in range(N)]))
# 영단어가 들어오면, 단어의 길이순 > 사전 순 으로 정렬
li.sort(key=lambda x : (len(x),x))
[print(i) for i in li]
# list comprehension