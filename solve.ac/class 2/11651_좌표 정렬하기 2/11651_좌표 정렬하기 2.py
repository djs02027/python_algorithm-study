
N=int(input())
arr=[]
for i in range(N):
    x,y=map(int,input().split())
    arr.append([x,y])
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

for a in arr:
    print(' '.join(map(str,a)))