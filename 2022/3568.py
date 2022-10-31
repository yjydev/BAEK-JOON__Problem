## iSharp      

sen = input().split( )
base = sen[0]
del sen[0]
for s in sen:
    s = s.replace(',', '').replace(';', '')
    res = base
    for i in range(len(s)-1,0,-1):
        t = s[i]
        if not t.isalpha():
            if t == ']':
                res += '[]'
            elif t == '[':
                continue
            else:
                res += t
    res += ' '
    for j in range(len(s)):
        if s[j].isalpha():
            res += s[j]
    print(res + ';')
