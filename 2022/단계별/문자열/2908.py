#상수
# A,B = input().split( )
# print(max(int(''.join(reversed(A))), int(''.join(reversed(B)))))

print(max(input()[::-1].split( ))) # [::-1] 이면 처음부터 끝까지 -1(역순 1칸씩)씩 돌리는 것