N, M = map(int,input().split())

floor = [list(input()) for _ in range(N)]
result = 0

# | 나 - 가 처음 나오면 +1, 이전 문자열 갱신하면서, - 인데 이전 문자열이 | 이거나, 반대인 경우 찾으면 + 1 (즉, 연속이 깨지면 +1)
# - 탐색 (행)
for i in range(N):
    previous = '/'      # 이전 문자열 초기화
    for j in range(M):
        if floor[i][j] == '-':
            if floor[i][j] != previous:     # 이전 문자열과 다르다면 개수 + 1
                result += 1
        previous = floor[i][j]      # 이전 문자열 갱신

# | 탐색 (열)
for i in range(M):
    previous = '/'
    for j in range(N):
        if floor[j][i] == '|':
            if floor[j][i] != previous:
                result += 1
        previous = floor[j][i]

print(result)



