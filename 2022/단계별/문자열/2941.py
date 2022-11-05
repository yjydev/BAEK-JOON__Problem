#크로아티아 알파벳
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
K = input()
res = 0
for c in cro:
    if c in K:
        while c in K:
            K = K.replace(c, ' ', 1)   
            # ''로 replace 하면, nljj 같은 경우 `n, lj, j` 로 분류해야하는데 
            # 'lj'가 제거되고 'nj'가 남아서 `lj,nj` 로 분류되는 예외 경우 존재 => 공백으로 분리하여 구분
            res += 1
print(res+len(K.replace(' ','')))