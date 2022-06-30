from collections import deque


def bfs(x):
    visited = [0] * (N + 1)
    q = deque()
    visited[x] = 1
    q.append(x)
    maxList = [0, 0]
    while q:
        idx = q.popleft()
        for ti, tl in tree[idx]:
            if visited[ti] == 0:
                visited[ti] = visited[idx] + tl
                q.append(ti)
                if maxList[0] < visited[ti]:
                    maxList = visited[ti], ti
    return maxList


N = int(input())
tree = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    tmpList = list(map(int, input().split()))
    n = tmpList[0]
    for j in range(1, len(tmpList) - 2, 2):
        tree[n].append((tmpList[j], tmpList[j + 1]))

distance, v = bfs(1)
distance, v = bfs(v)
print(distance - 1)
