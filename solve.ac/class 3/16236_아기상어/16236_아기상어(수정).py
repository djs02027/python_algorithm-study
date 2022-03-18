import sys
from collections import deque
input=sys.stdin.readline
dr=[-1,0,0,1]
dc=[0,-1,1,0]

def BFS(x,y):
    checkvisited = [[0 for _ in range(N)] for _ in range(N)]
    checkvisited[x][y]=0
    q=deque([[x,y]])
    visited=set([(x,y)])

    eating=0
    feed=False
    total=0
    babyshark=2
    while q:
        # q = deque(sorted(q))
        #q = deque(sorted(q, key=lambda k: [k[1], k[0]]))
        now=q.popleft()
        x,y=now[0],now[1]
        if field[x][y]!=0 and field[x][y]<babyshark:
            field[x][y]=0
            eating+=1


            if eating==babyshark:
                babyshark+=1
                eating=0


            q=deque()
            # q = deque(sorted(q, key=lambda k: (k[0], k[1])\\\\\\))
            visited=set([(x,y)])
            total += checkvisited[x][y]
            checkvisited = [[0 for _ in range(N)] for _ in range(N)]
            checkvisited[x][y] = 0
        # print(babyshark)
        # print(eating)
        print(field)
        print(now)
        print(q)
        # print(visited)
        #
        print(total)
        # print(checkvisited)

        for i in range(4):
            cx=x+dr[i]
            cy=y+dc[i]

            if 0<=cx<N and 0<=cy<N and not (cx,cy)  in visited:
                # print(cx, cy)
                if field[cx][cy]<=babyshark:
                    q.append([cx,cy])

                    visited.add((cx,cy))
                    checkvisited[cx][cy]=checkvisited[x][y]+1


####################


    return total


N=int(input().rstrip())
field=[list(map(int,input().rstrip().split())) for _ in range(N)]


start_x, start_y=0,0
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == 9:
            start_x=i
            start_y=j
            field[i][j] = 0
print(BFS(start_x,start_y))
