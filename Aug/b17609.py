def check(target, left, right):
    while left < right:   # 왼쪽 인덱스가 오른쪽 인덱스보다 커진다는 것은 전체의 절반 넘게 탐색한 것이므로 반복 종료
        if target[left] == target[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def check_2(target, left, right):
    while left < right:
        if target[left] == target[right]:
            left += 1
            right -= 1
        else:
            check_left = check(target, left+1, right) # 유사회문탐색 - 왼쪽 하나 무시
            check_right = check(target, left, right-1) # 유사회문탐색 - 오른쪽 하나 무시
            if check_left or check_right :
                return 1
            else:
                return 2
    return 0

T = int(input())
ans = []
for _ in range(T):
    num = list(input())
    result = check_2(num,0,len(num)-1)
    print(result)




# 시간초과 1
T = int(input())
for _ in range(T):
    result = 0 
    num = list(input())
    while len(num) > 1:
        if num[0] == num[-1]:
            num = num[1:-1]
        elif num[0] == num[-2]:
            num = num[1:-2]
            result = 1
        elif num[-1] == num[1]: 
            num = num[2:-1]
            result = 1
        else:
            result = 2
            break
    print(result)

# 시간초과 2
import sys

def check(target):
    while len(target)>1:
        if target[0] == target[-1]:
            target = target[1:-1]
        else:
            return False
    return True

def check_2(target):
    while len(target) > 1:
        if target[0] == target[-1]:
            target = target[1:-1]
        else:
            check_left = check(target[1:])
            check_right = check(target[:-1])
            if check_left or check_right :
                return 1
            else:
                return 2
    return 0

T = int(input())
for _ in range(T):
    num = list((sys.stdin.readline()).rstrip('\n'))
    result = check_2(num)
    print(result)
        