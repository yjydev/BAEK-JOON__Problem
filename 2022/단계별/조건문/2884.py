# 알람 시계
H,M = list(map(int,input().split( )))
if M >= 45:
    print(H,M-45)
elif H < 1:
    print(H-1+24, M+60-45)
else:
    print(H-1,M+60-45)