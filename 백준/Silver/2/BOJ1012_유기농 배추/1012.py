import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def BFS(x,y):

    for i in range(4):
        cx=x+deltax[i]
        cy=y+deltay[i]
        if 0<=cx<N and 0<=cy<M and plant[cx][cy]==1 and visited[cx][cy]==0:
            visited[cx][cy] = 1
            BFS(cx,cy)



    return 0


T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    plant = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        plant[j][i] = 1

    deltax = [1, -1, 0, 0]
    deltay = [0, 0, -1, 1]

    cnt=0
    for i in range(N):
        for j in range(M):
            if plant[i][j]==1 and visited[i][j]==0:
                BFS(i,j)
                cnt+=1

    print(cnt)


