def add(s,e,i):
    if s==e:
        tree[i].append(num[s])
        return
    mid = (s+e)//2
    tree[i].append(num[mid])
    add(s, mid-1, i+1)
    add(mid+1, e, i+1)


K = int(input())
num = list(map(int,input().split()))
tree = [[] for _ in range(K)]
n = len(num)
add(0,n-1, 0)

for t in tree:
    print(' '.join(map(str, t)))




# 중위순회 이용해서 시도
# K = int(input())
# num = list(map(int,input().split()))
# tree = [[] for _ in range(K+1)]
# left = [0] + [1] * ((2**(K-1))-1)
# right = [0] + [1] * ((2**(K-1))-1)
# i = 0
#
# def inorder(n, k):
#     global i, tree
#     if n and k <= K:
#         inorder(left[n], k+1)
#         tree[k].append(num[i])
#         i += 1
#         inorder(right[n], k)
#
# inorder(1,1)
# print(tree)


# 반복문 이용해서 시도
# -> 겉에 있는 노드들만 인식가능  = 가운데 있는 애들은 깊이 2인 트리까지만 가능
# 그냥 이진탐색 하는 것처럼 하면..?

# def add(li,i,n):
#     tree[i].append(li[n])
#
#
# K = int(input())
# num = list(map(int,input().split()))
# tree = [[] for _ in range(K)]
# n = len(num)
# n //= 2
# add(num,0,n)
# left = num[:n]
# right = num[n+1:]
# left_right= []
# right_left= []
#
# for i in range(K-1):
#     n //= 2
#     if len(left) == 1:
#         add(left,i+1,n)
#         if left_right:
#             add(left_right, i+1, n)
#         left = left[:n]
#         if right_left:
#             add(right_left, i+1, n)
#         add(right,i+1,n)
#         right = right[n + 1:]
#     else:
#         add(left, i + 1, n)
#         if left_right:
#             add(left_right, i + 1, n)
#         if right_left:
#             add(right_left, i+1, n)
#         add(right, i + 1, n)
#         left_right = left[n + 1:]
#         left = left[:n]
#
#         right_left = right[:n]
#         right = right[n + 1:]
#
#
# for t in tree:
#     print(' '.join(map(str, t)))