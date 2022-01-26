N=int(input())
arr=[0]*N
for _ in range(N):
    num=int(input())
    arr[num]+=1
start=0

for a in range(len(arr)):
    if arr[a]:
        for i in range(arr[a]):
            print(a)