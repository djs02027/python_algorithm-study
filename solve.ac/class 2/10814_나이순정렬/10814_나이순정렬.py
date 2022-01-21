arr=[]
N=int(input())
for i in range(N):

    arr.append(list(input().split()))

arr.sort(key=lambda a:int(a[0]))


for i in arr:
    print(' '.join(map(str,i)))