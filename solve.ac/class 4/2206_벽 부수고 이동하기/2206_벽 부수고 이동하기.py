#BFS는 최단거리를 찾자마자 종료할 수 있다.
#하지만 DFS는 모든 경로를 검색해 봐야 한다.


from collections import deque

moveCol = [1, -1, 0, 0]
moveRow = [0, 0, 1, -1]


def BFS(x, y, z):
    q = deque()
    q.append((x, y, z))
    visited[x][y][z] = 1


    while q:
        x, y, z = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]
        for i in range(4):
            cr = y + moveRow[i]
            cc = x + moveCol[i]
            if 0 <= cr < M and 0 <= cc < N:
                if field[cc][cr] == 0 and visited[cc][cr][z] == 0:
                    visited[cc][cr][z] = visited[x][y][z] + 1
                    q.append((cc, cr, z))
                elif field[cc][cr] == 1 and z == 1:
                    visited[cc][cr][0] = visited[x][y][1] + 1
                    q.append((cc, cr, 0))

    return -1


N, M = map(int, input().split())

field = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
print(BFS(0, 0, 1))


