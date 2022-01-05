import sys
sys.stdin = open('input.txt')
N, W = map(int, input().split())
tree = [[] * (N + 1) for _ in range(N + 1)]
Wtank = [0] * (N + 1)
Wtank[1] = W

for i in range(N - 1):
    U, V = map(int, input().split())
    if U < V:  # U가 부모
        tree[U].append(V)
        tree[U].sort()
    else:
        tree[V].append(U)
        tree[V].sort()
print(tree)
# for i in range(N + 1):
#     for j in range(len(tree[i])):
#         if tree[i]:
#             Wtank[tree[i][j]]= Wtank[i] // len(tree[i])

