N = int(input())
tree = {}

def preorder(n):
    if n != '.':
        print(n, end='')
        preorder(tree[n][0])
        preorder(tree[n][1])

def inorder(n):
    if n!= '.':
        inorder(tree[n][0])
        print(n, end='')
        inorder(tree[n][1])

def postorder(n):
    if n!= '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n, end='')


for i in range(N):
    a, b, c = input().split()
    tree[a] =[b,c]

preorder('A')
print()
inorder('A')
print()
postorder('A')


# 트리 내 값이 알파벳이면 리스트로 접근이 힏드므로 딕셔너리 활용 추천