import sys
N = int(input())
book_list =[int(sys.stdin.readline())]
cnt = 0
for k in range(1,N):
    book_list.append(int(sys.stdin.readline()))

for i in range(N):
    if book_list[-1-i] == N:
        N -= 1
    else:
        cnt += 1
print(cnt)

# 아이디어 -> 순서대로 정렬하면 맨 밑 책의 번호는 책의 개수와 같을 것, 아니라면 정렬해야하므로 횟수 +1