from collections import  Counter
N=int(input())
arr=[]

for _ in range(N):
    i=int(input())
    arr.append(i)
print(round(sum(arr)/N))

arr.sort()
if len(arr)%2==0:
    tmpnum = N // 2
    rd = tmpnum
    print(arr[rd-1])
else:
    tmpnum=(N//2)+1
    rd=tmpnum
    print(arr[rd-1])


cacmin=Counter(arr)
maxv=max(cacmin.values())
total=[]
for k, v in cacmin.items():
    total.append([k,v])

cnt=0
for i in range(len(total)):
    if total[i][1]==maxv:
        cnt+=1

if cnt>1:
    mintmp=4000
    for i in range(len(total)):
        if maxv==total[i][1]:
            if mintmp>=total[i][0]:
                mintmp=total[i][0]
    # print(mintmp)
    for i in range(len(total)):
        if mintmp==total[i][0]:
            total[i][0]=4000
    minvv=4000
    # print(total)
    for i in range(len(total)):
        if minvv>=total[i][0] and maxv==total[i][1]:
            minvv=total[i][0]
    print(minvv)
elif cnt==1:
    for i in range(len(total)):
        if maxv==total[i][1]:
            print(total[i][0])


result=max(arr)-min(arr)
print(result)

