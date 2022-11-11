# 수 정렬하기2
# 내장함수 사용 + 시간초과로 인해 sys 모듈 사용
import sys
N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
print(*sorted(li))


