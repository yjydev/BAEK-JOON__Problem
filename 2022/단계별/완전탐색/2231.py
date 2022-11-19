# 분해합
N = int(input())
# 198 => 198 + 1 + 9 + 8 = 216 이므로 198은 216의 생성자이다.
# 이 상황에서 생성자 후보 중 최소값은 216 - (9*자릿수) 이다.
# 각 자릿수의 합을 더하는건데 자릿수는 최대가 9이므로.
for i in range(max(1,N-(len(str(N))*9)),N):
    tmp = i + sum(list(map(int,str(i))))
    if N == tmp:
        print(i)
        break
else:
    print(0)
