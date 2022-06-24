import sys
sys.setrecursionlimit(10000)


def DFS(n):
    visited[n] = 1
    for c in checkList[n]:
        if not visited[c]:
            DFS(c)


N, M = map(int, input().split())
checkList = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 0
for _ in range(M):
    u, v = map(int, input().split())
    checkList[u].append(v)
    checkList[v].append(u)
for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        count += 1
print(count)
