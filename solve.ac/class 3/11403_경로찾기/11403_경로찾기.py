from collections import deque


def BFS(x, y):
    visited[i][j]=1
    visited[j][i]=1





N = int(input())
q = deque()
Field = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if Field[i][j] == 1:
            BFS(i, j)
print(visited)