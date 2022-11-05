#그룹 단어 체커
N = int(input())
res = 0
for n in range(N):
    words = input()
    li = set(words)
    cur = ''
    for word in words:
        if word in li:
            cur = word
            li.remove(word)
        elif word == cur:
            continue
        else:
            break
    else:
        res+=1
print(res)