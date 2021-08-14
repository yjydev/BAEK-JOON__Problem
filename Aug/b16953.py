N, target = map(int, input().split())
cnt = 0
while target != N :
    if target < N:
        cnt = -2
        break
    elif str(target)[-1] == '1':
        target = int(str(target)[:-1])
        cnt += 1
    elif not target % 2 :
        target = int(target // 2)
        cnt += 1
    else:
        cnt = -2
        break
print(cnt+1)

# 사용한 반례
# N, target = 1 3 (if분기 아무것도 타지 않는경우 무한반복) - else분기 추가
# N, target = 5 102 (조건문 순서 오류) - if 분기를 elif 분기로 변경
# -> 102 /2 = 51 다음에 51 -[1] = 5로 if분기 타는데 다음 if 분기가 2로 나뉘는지여서 else 분기를 타게되니까 -1 을 출력하는 오류 발생 

# 최소값에 1 더한 값 출력해야해서 target < N 분기 따로 만들어서 -2하고 최종에 +1
# 처음엔 문자열이 수정불가하다고 슬라이싱도 안된다고 착각하고 구현해서 시간초과