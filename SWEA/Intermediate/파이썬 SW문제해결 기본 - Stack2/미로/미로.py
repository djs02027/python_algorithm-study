def FindEnd(sx, sy):
    global flag
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if Map[sx][sy] == 3:
        flag = 1
    for i in range(4):
        cx = sx + dx[i]
        cy = sy + dy[i]
        if 0 <= cx < N and 0 <= cy < N and Map[cx][cy] != 1:
            if visited[cx][cy] == 0:
                visited[cx][cy] = 1
                FindEnd(cx, cy)
                visited[cx][cy] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Map = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sx, sy = 0, 0
    flag = 0
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 2:
                sx = i
                sy = j
    visited[sx][sy] = 1
    FindEnd(sx, sy)
    print('#{} {}'.format(tc, flag))