import sys
input = sys.stdin.readline
def DFS(s, e, c):
    global minV
    visited[s][e] = 1
    # print(visited)

    if e==(M-1) and s==(N-1):
        if minV>c:
            minV=c

    for i in range(4):
        cr = e + dr[i]
        cc = s + dc[i]
        if 0 <= cr < M and 0 <= cc < N:
            if Map[cc][cr] == 1 and  visited[cc][cr]==0:

                DFS(cc, cr, c + 1)
                visited[cc][cr]=0


N, M = map(int, input().rstrip().split())
minV=9999999999
start, end = 0, 0
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
Map = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0]=1
DFS(start, end, 1)


print(minV)