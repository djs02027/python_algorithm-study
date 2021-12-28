# 트리의 각 정점에는 1번부터 N번까지 번호가 붙어있다
# 자식이 없는 노드는 '리프 노드'
# 어떤 사람의 차례가 오면, 그 사람은 현재 존재하는 게임말 중 아무거나
# 하나를 골라 그 말이 놓여있던 노드의 부모 노드로 옮긴다.
#  루트 노드에 도착했다면 그 게임말을 즉시 제거한다. 모
#  모든 과정을 마치면 다음 사람에게 차례를 넘긴다
#  선 - 성원

import sys

sys.stdin = open('input.txt')
N = int(input())
link = [[] for _ in range(N + 1)]
directions =[[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    link[a].append(b)
    directions[b].append(a)
visited = [0] * (N + 1)
print(link)
cnt = 0
leap = []
for i in range(N, -1, -1):
    for j in range(len(link[i])):
        if not link[link[i][j]]:
            leap.append(link[i][j])
print(leap)
print(directions)
total=0
for lp in leap:
    tmp=lp
    while True:
        if tmp==1:
            break
        else:
            tmp=directions[tmp][0]
            total += 1

print(total)