L, C = map(int, input().split())        # L 은 암호에 사용된 소문자 개수, C 는 암호 가능성있는 소문자 개수
chars = input().split()

vowel = ['a','e','i','o','u']
chars.sort()

def check(num):
    if len(ch) == L:
        cnt = cnt_1 = 0
        for n in ch:
            if n in vowel:
                cnt += 1            # 모음 수
            else:
                cnt_1 += 1          # 자음 수
        if cnt >= 1 and cnt_1 >= 2:
            print(''.join(map(str, ch)))
            return
    else:
        for i in range(len(num)):
            ch.append(num[i])
            check(num[i+1:])
            if ch:
                ch.pop(-1)


ch = []
check(chars)

# cnt랑 cnt_1 은 자음모음 갯수세는거니까 매번 초기화해줬어야 했는데, 지역변수로 선언하고 초기화 안해줘서 계속 틀렸음..
# 도움 된 반례 >
# 3 6
# a b c d e f









