# 재귀 없이 반복문 구현

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    li = [list(map(int,input().split())) for _ in range(N)]
    tree = [[] for _ in range(N+1)]
    for i in range(N-1):
        A,B = li[i]
        tree[B].append(A)           # 부모를 찾는것이므로 자식번호를 인덱스로 하는게 훨씬 편함
    target = li[N-1]
    candidates_1 = [target[0]]
    candidates_2 = [target[1]]
    n = target[0]
    while tree[n]:
        candidates_1.append(tree[n][0])
        n = tree[n][0]
    n = target[1]
    while tree[n]:
        candidates_2.append(tree[n][0])
        n = tree[n][0]
    for r in candidates_1:
        if r in candidates_2:
            print(r)
            break


# 재귀 깊이 임의로 늘린것 -> 늘리면 통과, 안늘리면 RecursionError 발생

# import sys
# sys.setrecursionlimit(10**9)
#
# def find_parent(n, li):
#     if tree[n]:
#         li.append(tree[n][0])
#         find_parent(tree[n][0], li)
#         return
#     else:
#         return
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     li = [list(map(int,input().split())) for _ in range(N)]
#     tree = [[] for _ in range(N+1)]
#     for i in range(N-1):
#         A,B = li[i]
#         tree[B].append(A)           # 부모를 찾는것이므로 자식번호를 인덱스로 하는게 훨씬 편함
#     target = li[N-1]
#     candidates_1 = [target[0]]
#     candidates_2 = [target[1]]
#     find_parent(target[0], candidates_1)
#     find_parent(target[1], candidates_2)
#     for r in candidates_1:
#         if r in candidates_2:
#             print(r)
#             break



