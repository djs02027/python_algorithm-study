import sys

sys.stdin = open('Input.txt'
                 )


def preorder(node):
    print(node.item, end="")
    if node.lc != '.':
        preorder(tree[node.lc])
    if node.rc != '.':
        preorder(tree[node.rc])


def inorder(node):
    if node.lc != '.':
        inorder(tree[node.lc])
    print(node.item, end="")
    if node.rc != '.':
        inorder(tree[node.rc])


def postorder(node):
    if node.lc != '.':
        postorder(tree[node.lc])
    if node.rc != '.':
        postorder(tree[node.rc])
    print(node.item, end="")


# 노드 구조체 선언
class Node:
    def __init__(self, item, lc, rc):
        self.item = item
        self.lc = lc
        self.rc = rc


N = int(input())
left = []
right = []
tree = {}
for i in range(N):
    p, cl, cr = map(str, input().split())
    tree[p] = Node(item=p, lc=cl, rc=cr)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])