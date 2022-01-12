from collections import  Counter
N=int(input())
arr=[]

for _ in range(N):
    i=int(input())
    arr.append(i)
print(sum(arr)//N)
arr.sort()
print(arr[N//2])


cacmin=Counter(arr)


print(cacmin)

result=max(arr)-min(arr)
print(result)