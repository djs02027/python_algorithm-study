def BFS(x, y, visitied):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if Map[x][y] == 3:
        return

    else:
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < N and 0 <= cy < N and Map[cx][cy] != 1:
                if visitied[cx][cy] == 0:
                    visitied[cx][cy] = visitied[x][y] + 1
                    BFS(cx, cy, visitied)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]
    visitied = [[0] * N for _ in range(N)]

    sx, sy = 0, 0
    ex, ey = 0, 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2:
                sx, sy = i, j
            if Map[i][j] == 3:
                ex, ey = i, j
    visitied[sx][sy] = 1
    BFS(sx, sy, visitied)
    if visitied[ex][ey]:
        print('#{} {}'.format(tc, visitied[ex][ey]-2))
    else:
        print('#{} {}'.format(tc, visitied[ex][ey]))
