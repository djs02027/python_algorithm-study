import sys

sys.stdin = open('input.txt')
N = int(input())
root = list(map(int, input().split()))
cutter = int(input())

MaxV = -1
if cutter + 2 <= len(root) and cutter + 1 <= len(root):
    root[cutter + 1] = -1
    root[cutter + 2] = -1

for i in range(len(root)):
    if MaxV < root[i]:
        MaxV = root[i]
cnt = 0
for i in range(len(root)):
    if MaxV == root[i]:
        cnt += 1
if cutter == root[0]:
    cnt = 0
print(cnt)
