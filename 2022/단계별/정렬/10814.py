#나이순 정렬
N = int(input())
members = [list(input().split()) for _ in range(N)]
members.sort(key=lambda x : int(x[0])) # 나이 증가순 or 원래 그대로 정렬
[print(m[0],m[1]) for m in members]

# 시간이 4044ms 라서 수정의 필요성을 느낍니다..