# 오븐 시계
cur_H, cur_M = list(map(int,input().split( )))
cook_M = int(input())
cur_M += cook_M
print((cur_H+(cur_M//60))%24, cur_M%60)
