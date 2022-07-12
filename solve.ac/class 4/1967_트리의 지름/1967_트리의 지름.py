# "그래프일 경우" :
# 간선의 가중치가 모두 동일 -> BFS
# 그렇지 않은 경우 -> 다익스트라
#
# "트리인 경우" :
# DFS or BFS
from collections import deque


def BFS(x):
    visited = [0] * (N + 1)
    visited[x] = 1
    q = deque()
    q.append(x)
    maxvalue = [0, 0]
    while q:
        now = q.popleft()
        for next, value in tree[now]:
            if visited[next] == 0:
                visited[next] = visited[now] + value
                q.append(next)
                if maxvalue[0] < visited[next] :
                    maxvalue[0] = visited[next]
                    maxvalue[1] = next
    return maxvalue


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
    s, e, v = map(int, input().split())
    tree[s].append((e, v))
    tree[e].append((s, v))

distance, v = BFS(1)
distance, v = BFS(v)
result= distance-1
if result<0:
    print(0)
else:
    print(result)