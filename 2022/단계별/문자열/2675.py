#문자열 반복
# T = int(input())
# for _ in range(T):
#     R,S = input().split( )
#     P = ''
#     for s in S:
#         P += s*int(R)
#     print(P)

T = int(input())
for _ in range(T):
    R,S = input().split( )
    print(''.join(s*int(R) for s in S))