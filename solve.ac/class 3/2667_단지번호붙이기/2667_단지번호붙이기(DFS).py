# 상 하 좌 우
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def DFS(x, y):
    global cnt
    visited[x][y] = 1
    if mapField[x][y] == 1:
        cnt += 1
    for k in range(4):
        cc = dc[k] + x
        cr = dr[k] + y

        if 0 <= cc < N and 0 <= cr < N:
            if visited[cc][cr] == 0 and mapField[cc][cr] == 1:
                DFS(cc, cr)


N = int(input())

mapField = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
cnt = 0
result=[]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and mapField[i][j] == 1:
            DFS(i, j)
            result.append(cnt)
            cnt=0

print(len(result))
result.sort()
for r in result:
    print(r)