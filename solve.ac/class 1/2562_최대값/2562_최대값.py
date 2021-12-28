arr=[]
for i in range(9):
    num=int(input())
    arr.append(num)
idx = 0
maxv=-1
for i in range(9):
    if arr[i]>maxv:
        maxv=arr[i]
        idx=i
print(maxv)
print(idx+1)