x,y,w,h=map(int, input().split())
L1,L2=0,0
Rx=w-x
Ry=h-y
Lx=x-L1
Ly=y-L2
print(min(Rx,Ry,Lx,Ly))