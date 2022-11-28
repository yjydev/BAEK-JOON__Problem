#나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
poketmon = {}  # 번호(key)로 이름(value) 찾기
poket_rev = {}  # 이름(key)으로 번호(value) 찾기
for i in range(N):
    # sys.stdin.readline으로 글자 하나씩 입력받을 때는 
    # 오른쪽끝에 개행 문자 \n 가 포함되기 때문에 rstrip() 필수
    a = input().rstrip()
    poketmon[str(i+1)] = a
    poket_rev[a] = i+1
for _ in range(M):
    problem = input().rstrip()
    if problem.isdigit():
        print(poketmon[problem])
    else:
        print(poket_rev[problem])




# 8%... 시간 초과 => input 받을 때 오래걸려서 발생 => sys 모듈 이용하면 해결
# poketmon = {}
# poket_rev = {}
# for i in range(N):
#     a = input()
#     poketmon[str(i+1)] = a
#     poket_rev[a] = i+1
# for _ in range(M):
#     problem = input()
#     if problem in list(poketmon.keys()):
#         print(poketmon[problem])
#     else:
#         print(poket_rev[problem])


# 8%... 시간초과 => index는 best O(1), worst O(n)
# poketmon = [input() for _ in range(N)]
# for _ in range(M):
#     problem = input()
#     try :
#         problem = int(problem)
#         print(poketmon[problem-1])
#     except:
#         print(poketmon.index(problem)+1)