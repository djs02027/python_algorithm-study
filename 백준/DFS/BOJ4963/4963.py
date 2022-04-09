import sys
#	런타임 에러 (RecursionError)
# 재귀 깊이 설정하는 함수
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')
#       좌 우 하 상 대각선..
delx = [0, 0, 1, -1, -1, -1, 1, 1]
dely = [-1, 1, 0, 0, -1, 1, -1, 1]


def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        cx = delx[i] + x
        cy = dely[i] + y
        if 0 <= cx < H and 0 <= cy < W:
            if arr[cx][cy] == 1 and not visited[cx][cy]:
                dfs(cx, cy)


while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    cnt=0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt+=1
    print(cnt)
