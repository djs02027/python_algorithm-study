from collections import deque


def topology_sort():
    global result
    q = deque()
    for i in range(1, N + 1):
        if linked[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for g in graph[now]:
            linked[g] -= 1
            if linked[g] == 0:
                q.append(g)


N, M = map(int, input().split())
linked = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
result = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    linked[b] += 1
topology_sort()
for r in result:
    print(r, end=" ")
