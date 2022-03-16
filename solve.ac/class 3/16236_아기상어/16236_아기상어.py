import sys
from collections import deque
input=sys.stdin.readline
dr=[-1,0,0,1]
dc=[0,-1,1,0]

def BFS(x,y):

    q=deque([[x,y]])
    visited=[[x,y]]
    time=0
    eating=0
    eat_flag = False
    total=0
    babyshark=2
    while q:
        # q = deque(sorted(q))
        q = deque(sorted(q, key=lambda k: [k[1], k[0]]))

        qSize=len(q)
        for _ in range(qSize):
            now=q.popleft()
            x,y=now[0],now[1]

            if 0<field[x][y]<babyshark:
                field[x][y]=0
                eating+=1
                if eating==babyshark:
                    babyshark+=1
                    eating=0


                q=deque()
                visited=[[x,y]]
                total = time
                eat_flag = True
            # print(babyshark)
            # print(eating)
            #print(field)
            print(now)
            print(q)
            # print(visited)
            #
            print(total)


            for i in range(4):
                cx=x+dr[i]
                cy=y+dc[i]

                if  0<=cx<N and 0<=cy<N and not [cx,cy] in visited:
                    # print(cx, cy)
                    if field[cx][cy] <= babyshark:
                        q.append([cx,cy])
                        visited.append([cx,cy])

            if eat_flag:
                eat_flag=False
                break


        time+=1
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
