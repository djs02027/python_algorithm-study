import sys
from heapq import heappop, heappush
input = sys.stdin.readline


dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
q = []


def BFS():
    visited = [[0] * N for _ in range(N)]
    eating = 0
    total = 0
    babyshark = 2

    while q:

        d, x, y = heappop(q)

        if 0 < field[x][y] < babyshark:
            field[x][y] = 0
            eating += 1

            if eating == babyshark:
                babyshark += 1
                eating = 0

            total += d
            d = 0

            while q:
                q.pop()

            visited = [[0] * N for _ in range(N)]


        for i in range(4):
            cx = x + dr[i]
            cy = y + dc[i]
            dx = d + 1


            if 0 <= cx < N and 0 <= cy < N and visited[cx][cy]==0 and field[cx][cy] <= babyshark:
                # print(cx, cy)
                heappush(q, (dx, cx, cy))
                visited[cx][cy] = 1

    return total



N = int(input().rstrip())
field = [list(map(int, input().rstrip().split())) for _ in range(N)]

start_x, start_y = 0, 0
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == 9:
            start_x = i
            start_y = j
            heappush(q, (0, start_x, start_y))
            field[i][j] = 0

result=BFS()
print(result)
