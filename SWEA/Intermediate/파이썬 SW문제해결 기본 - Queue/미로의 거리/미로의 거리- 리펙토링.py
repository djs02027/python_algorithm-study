def BFS(sx, sy):
    global cnt
    q = [sx, sy]
    visited[sx][sy] = 1
    while q:
        nowx = q.pop(0)
        nowy = q.pop(0)
        for i in range(4):
            x = nowx + dx[i]
            y = nowy + dy[i]
            if x >= 0 and y >= 0 and x < N and y < N:
                if miro[x][y] == 0 and visited[x][y] == 0:
                    q.append(x)
                    q.append(y)
                    miro[x][y] = 1
                    visited[x][y] = visited[nowx][nowy] + 1

                if miro[x][y] == 3 and visited[x][y] == 0:
                    return visited[nowx][nowy] - 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    # print(miro)
    sx = 0
    sy = 0
    cnt = 0
    visited = [[0] * (N) for _ in range(N)]
    for i in range(0, N):
        for j in range(0, N):
            if miro[i][j] == 2:
                sx = i
                sy = j
        if sx and sy:
            break
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    print('#{} {}'.format(tc, BFS(sx, sy)))
