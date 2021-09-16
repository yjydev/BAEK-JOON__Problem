import sys

N,M = map(int, sys.stdin.readline().split())
yard = [0] + list(map(int,sys.stdin.readline().split()))

result = 0

# 그냥 모든 경우의 수를 탐색하는걸로..굴+굴+굴+굴+점 , 굴+굴+굴+점, 굴+점+굴+굴 등등..
def dfs(i, size, sec):
    global result
    if sec > M :
        return
    else:
        result = max(result,size)
        if i <= N-1:
            dfs(i+1,size+yard[i+1],sec+1)
        if i <= N-2:
            dfs(i+2,size//2 + yard[i+2],sec+1)

dfs(0,1,0)
print(result)



