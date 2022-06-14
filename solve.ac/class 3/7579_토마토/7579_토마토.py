from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = box

q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append([i, j, k])

dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dh = [-1, 1, 0, 0, 0, 0]
maxTomato=-1
while q:
    h, n, m = q.popleft()
    if visited[h][n][m]>maxTomato:
        maxTomato=visited[h][n][m]
    for i in range(6):
        ch = h + dh[i]
        cn = n + dx[i]
        cm = m + dy[i]
        if 0 <= ch < H and 0 <= cn < N and 0 <= cm < M and not visited[ch][cn][cm]:
            visited[ch][cn][cm] = visited[h][n][m] + 1
            q.append([ch, cn, cm])

flag=0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if visited[i][j][k] == 0:
                flag=1
                break
        if flag==1:
            break
    if flag == 1:
        break
if flag==1:
    print(-1)
else:
    print(maxTomato-1)
