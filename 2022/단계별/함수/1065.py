#한수
N = int(input())
def is_diff(x):
    x = str(x)
    if len(x) == 1:
        return True
    li = list(map(int,x))
    diff = li[0]-li[1]
    for i in range(len(li)-1):
        if li[i]-li[i+1] != diff:
            return False
    return True 
print(len(list(filter(lambda x: is_diff(x) == True, [i for i in range(1,N+1)]))))
