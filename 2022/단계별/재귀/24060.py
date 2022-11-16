#알고리즘 수업 - 병합 정렬1
N, K = map(int,input().split())
li = list(map(int,input().split()))

def merge_sort(arr, s, e):
    global cnt, K
    if s < e and cnt <= K:
        q = (s+e)//2
        merge_sort(arr,s,q)
        merge_sort(arr,q+1,e)
        merge(arr,s,q,e)

def merge(arr, s, mid, e):
    global cnt, res
    i,j = s, mid+1
    tmp = []
    while i <= mid and j <= e: # i가 왼쪽에 있고, j가 오른쪽에 있는 상황이면
        # arr[i], arr[j] 중 더 작은 걸 tmp 에 추가하고 +1
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= mid:   # 왼쪽 배열이 남아 있는 경우
        tmp.append(arr[i])
        i += 1
    while j <= e:     # 오른쪽 배열이 남아 있는 경우
        tmp.append(arr[j])
        j += 1
    # arr 배열 갱신
    i, t = s, 0
    while i <= e:
        arr[i] = tmp[t]
        # 문제에서 구하고자 하는 K번째 저장 수를 찾기 위함
        cnt += 1
        if cnt == K:
            res = arr[i]
            return
        i += 1
        t += 1

cnt = 0
res = -1
merge_sort(li, 0, N-1)
print(res)
