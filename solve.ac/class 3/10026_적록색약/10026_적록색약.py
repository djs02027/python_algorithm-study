from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if picture[nx][ny] == picture[x][y] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])



N = int(input())
picture = [list(map(str, input())) for _ in range(N)]
q = deque()

visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'


visited = [[0] * N for _ in range(N)]

cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j)
            cnt2 += 1


print(cnt1, cnt2)
