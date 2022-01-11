N=int(input())
arr=list(map(int, input().split()))
M=max(arr)
checked=[True for _ in range(M+1)]
checked[1]=False
checked[0]=False
for i in range(2,M+1):
    if checked[i] == True:
        j=2
        while(i*j)<=M:
            checked[i*j]=False
            j+=1
cnt=0
for  a in arr:
    if checked[a]==True:
        cnt+=1

print(cnt)
