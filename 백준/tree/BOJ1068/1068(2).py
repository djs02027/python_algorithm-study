

import sys

sys.stdin = open('input.txt')
N = int(input())
node = list(map(int, input().split()))
tree = {}
cutter = int(input())

for i in range(N):
    if i == cutter or node[i] == cutter:
        continue
    if node[i] in tree:
        tree[node[i]].append(i)
        print(tree)
    else:
        tree[node[i]] = [i]
cnt=0
if -1 in tree:
    q=[-1]
else:
    q=[]
while q:
    n = q.pop()
    if n not in tree:
        cnt+=1
    else:
        q+= tree[n]
print(cnt)