from collections import deque
def findcell(c,r):
    global visited, dr,dc
    q=deque()
    q.append((c,r))
    visited[c][r] = 1
    tmp=1
    while q:
        nc,nr=q.popleft()
        for i in range(4):
            cr=dr[i]+nr
            cc=dc[i]+nc
            if 0<=cr<N and 0<=cc<N and field[cc][cr]==1 :
                if visited[cc][cr]==0:
                    visited[cc][cr]=1
                    q.append((cc,cr))
                    tmp+=1

    return tmp


N = int(input())
field = [list(map(int, input())) for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

visited = [[0] * N for _ in range(N)]
count=[]
total=0
for i in range(N):
    for j in range(len(field[i])):
        if field[i][j]==1 and visited[i][j]==0:
            result=findcell(i,j)
            count.append(result)
            total+=1

print(total)
count.sort()
for c in count:
    print(c)