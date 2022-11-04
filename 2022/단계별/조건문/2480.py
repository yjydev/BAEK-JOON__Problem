# 주사위 세개
a,b,c = list(map(int,input().split( )))
k = 0
if a == b == c :
    print(10000+a*1000)
else:
    k = a if a == b else (b if b == c else (a if a == c else print(max(a,b,c)*100)))
if k:
    print(1000+k*100)

# a,b,c = list(map(int,input().split( )))
# k = 0
# if a == b == c :
#     print(10000+a*1000)
# elif a == b:
#     k = a
# elif b == c:
#     k = b
# elif a == c:
#     k = a
# else:
#     print(max(a,b,c)*100)
# if k:
#     print(1000+k*100)