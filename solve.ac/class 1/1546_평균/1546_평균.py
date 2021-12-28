N=int(input())
arr=list(map(int,input().split()))

cac=0
maxv=max(arr)
for i in arr:
    result=(i/maxv)*100
    cac+=result
print("{:.2f}".format(cac/N))