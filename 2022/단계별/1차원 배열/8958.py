#OX퀴즈
T = int(input())
for t in range(T):
    res = input()
    score = 0
    start = 0
    for i,r in enumerate(res):
        if r == 'O':
            score += res[start:i+1].count('O')
        else:
            start = i
    print(score)
