import sys
from collections import deque
input=sys.stdin.readline
dr=[-1,0,0,0]
dc=[0,1,-1,1]
def findfeed(shark):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]<shark and field[i][j]!=0 and field[i][j]!=9:
                return True
    return False
def BFS(x,y):
    global babyshark
    q=deque([[x,y]])
    visited=set([(x,y)])
    print(q)
    print(visited)
    eating=0
    time=0
    total=0
    while q:
        q = deque(sorted(q))
        print(q)
        print(visited)
        now=q.popleft()
        x,y=now[0],now[1]
        if field[x][y]!=0 and field[x][y]!=9 and field[x][y]<babyshark:
            eating+=1

            if eating==babyshark:
                babyshark+=1
                eating=0

            # if not findfeed(babyshark):
            #         return time
            q=deque()
            visited=set([x,y])
            total = time
        for i in range(len(dr)):
            cx=x+dc[i]
            cy=y+dr[i]
            if 0<=cx<N and 0<=cy<N and (cx,cy) not in visited:
                if field[cx][cy]<=babyshark:
                    q.append([cx,cy])
                    visited.add((cx,cy))

        print(time)

        time+=1
    return total


N=int(input().rstrip())
field=[list(map(int,input().rstrip().split())) for _ in range(N)]

babyshark=2
start_x, start_y=0,0
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == 9:
            start_x=i
            start_y=j
if findfeed(babyshark):
    print(BFS(start_x,start_y))
else:
    print(0)