from collections import deque

# 상 하 좌 우
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            cc = dc[k] + x
            cr = dr[k] + y
            if 0 <= cc < N and 0 <= cr < N:
                if field[cc][cr]==1 and visited[cc][cr]==0:
                    q.append((cc,cr))
                    visited[cc][cr]=1
                    cnt+=1

    return cnt


N = int(input())
field = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer=[]
for i in range(N):
    for j in range(N):
        if field[i][j] == 1 and visited[i][j] == 0:
            result=bfs(i, j)
            answer.append(result)
print(len(answer))
answer.sort()
for a in answer:
    print(a)