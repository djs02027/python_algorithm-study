
M,S=map(int, input().split())
N=1000000
check=[True for _ in range(N+1)]
check[1]=False
for i in range(2,N+1):
    if check[i]==True:
        j=2
        while (i*j)<=N:
            check[i*j]=False
            j+=1
    if i==S:
        break

for i in range(M,S+1):

    if check[i]==True:
        print(i)