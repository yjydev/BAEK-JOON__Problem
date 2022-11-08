N, hp = map(int,input().split())
skil = []
for _ in range(N):
    c,d = map(int,input().split())
    skil.append([c,d,0])
skil.sort(key=lambda x: x[1], reverse=True)

t = -1
while hp > 0:
    pos = list(filter(lambda x: x[2] == 0, skil))
    npos = list(filter(lambda x: x[2] != 0, skil))
    for p in pos:
        hp -= p[1]
        p[2] = p[0]
    for n in npos:
        n[2] -= 1
    t += 1
print(t)