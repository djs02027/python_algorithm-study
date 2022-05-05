from collections import deque
M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
# 오 왼 하 상
dc = [0, 0, 1, -1]
dr = [1, -1, 0, 0]
red = deque()
for i in range(len(tomatos)):
    for j in range(len(tomatos[i])):
        if tomatos[i][j] == 1:
            red.append((i, j))
maxv=-1
cnt=0
while red:
    x, y = red.popleft()
    if tomatos[x][y]>maxv:
        maxv=tomatos[x][y]
    for i in range(4):
        cx = x + dc[i]
        cy = y + dr[i]
        if 0 <= cx < N and 0 <= cy < M:
            if tomatos[cx][cy] == 0:
                tomatos[cx][cy]=tomatos[x][y]+1
                red.append((cx, cy))


flag=0

for i in range(len(tomatos)):
    for j in range(len(tomatos[i])):
        if tomatos[i][j]==0:
            flag=1
            break
if flag==1:
    print(-1)
else:
    print(maxv-1)

