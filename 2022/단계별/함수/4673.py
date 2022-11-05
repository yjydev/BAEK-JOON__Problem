#셀프 넘버
def d(n):
    li = list(map(int,str(n)))
    return n+sum(li)
standard = {*range(1,10001)}
for i in range(1,10001):
    standard.discard(d(i))
print(*standard)
