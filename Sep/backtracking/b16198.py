N = int(input())
W = list(map(int,input().split()))
result = ans = 0

def check(w):
    global result, ans
    if len(w) == 2:
        return
    else:
        for i in range(1,len(w)-1):
        # 이전값과 다음값 곱한 값을 cal에 저장
            cal = w[i-1] * w[i+1]
        # result는 현재까지 모은 에너지값
            result += cal
        # 최대값 찾기
            ans = max(result, ans)
        # 구슬 제외
            t = w.pop(i)
        # 재귀
            check(w)
        # 길이가 2가 되서 리턴되어 나오고 나면, result 값에서 바로 이전에 더했던 값 빼기
            result -= cal
        # pop했던 값을 원상복귀하고 다시 체크
            w.insert(i,t)

check(W)
print(ans)