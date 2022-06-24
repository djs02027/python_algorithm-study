N=int(input())
LineList=list(map(int,input().split()))
LineList.sort()

total=0
for i in range(1,N+1):
    total=total+sum(LineList[:i])
print(total)