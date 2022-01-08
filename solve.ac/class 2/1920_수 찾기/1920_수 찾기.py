N=int(input())
arr1=list(map(int, input().split()))
M=int(input())
arr2=list(map(int, input().split()))

arr1=sorted(arr1)


result=0

for i in range(len(arr2)):
    flag=0
    start = 0
    end = N
    while start<=end:
        result=(start+end)//2
        if result>=N:
            break

        if arr1[result]<arr2[i]:
            start=result+1
        elif arr1[result]>arr2[i]:
            end=result-1
        elif arr1[result]==arr2[i]:
            flag=1
            break

    print(flag)
