N, M = map(int,input().split())

floor = [list(input()) for _ in range(N)]
result = 0

# - 탐색 (행)
for i in range(N):
    previous = '/'
    for j in range(M):
        if floor[i][j] == '-':
            if floor[i][j] != previous:
                result += 1
        previous = floor[i][j]

# | 탐색 (열)
for i in range(M):
    previous = '/'
    for j in range(N):
        if floor[j][i] == '|':
            if floor[j][i] != previous:
                result += 1
        previous = floor[j][i]

print(result)



