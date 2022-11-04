def check(num):
    global N
    mid = int(num ** 0.5)
    for i in range(2, mid + 1):     # 소수가 맞는지 검사하는 코드가 위에 있어야 걸러지므로
        if not num % i:
            return
    if len(str(num)) == N:          # 소수가 맞는데 N자리 수라면 조건에 맞으므로 출력
        print(num)
    else:
        for k in range(10):
            nums = num*10 + k       # 한 자리 추가해서 다시 소수인지 체크
            check(nums)

N = int(input())
pri = [2,3,5,7]
for p in pri:
    check(p)




