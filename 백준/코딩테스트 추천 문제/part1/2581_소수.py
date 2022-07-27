import math
def find_prime(n):
    isprime = [True] * (10002)
    for i in range(2,int(math.sqrt(n))+1):
        if isprime[i]==True:
            j=2
            while i*j<n:
                isprime[i*j]=False
                j+=1

    return [i for i in range(2,n+1) if isprime[i]]

M=int(input())
N=int(input())



result=find_prime(10001)
total=0
minv=int(1e9)
for r in result:
    if M<=r<=N:
        total+=r
        if minv>r:
            minv=r
if total==0:
    print(-1)
else:
    print(total)
    print(minv)


