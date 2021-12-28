arr=list(input())
check=[-1 for i in range(26)]
cnt=0
for i in range(len(arr)):
    if check[ord(arr[i])-97]==-1:
        check[ord(arr[i])-97]=cnt
    cnt+=1
print(' '.join(map(str,check)))
