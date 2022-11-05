#손익분기점 A+(B*x) < (170*x)
A,B,C = list(map(int,input().split()))
print(-1) if B >= C else print(A//(C-B)+1)  # B가 가변 비용, C가 이익인데 B > C 이면 
                        # 아무리 이익을 벌어도 가변 비용이 더 많이 들어서 수익을 낼 수 없다.
                        # B = C 여도 이익을 번 만큼 비용으로 나가는 것이니까 수익을 낼 수 없다.


# 첫 아이디어
# min_cnt = A//C
# if min_cnt*C < min_cnt*B:
#     print(-1)
# else:
#     A += B*min_cnt - C*min_cnt
#     while True:
