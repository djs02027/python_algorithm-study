T= int(input())
arr=[]
for i in range(T):
    N,M=map(int,input().split())
    arr.append([N,M])

total=[]
k=0
while True:
    cnt=0
    for i in range(len(arr)):
        if k==i:
            continue
        if k<len(arr) and arr[k][0] < arr[i][0] and arr[k][1] < arr[i][1]:
                cnt+=1

    total.append(cnt+1)
    k += 1

    if k == len(arr):
        break
result=" ".join(map(str,total))
print(result)