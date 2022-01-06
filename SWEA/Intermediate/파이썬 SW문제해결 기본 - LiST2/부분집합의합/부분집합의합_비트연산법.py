T = int(input())

for tc in range(1,T+1):

    N,K= map(int,input().split())

    arr=list(range(1,13))
    # print(arr)
    # for n in range(1, N + 1):
    #     arr.append(n)

    result=0
    for i in range(1 << 12):
        tmp=[]
        for j in range(13):
            if i & (1<<j):
                tmp.append(arr[j])
        if len(tmp)==N:
            if sum(tmp)==K:
                result +=1

    print('#{} {}'.format(tc, result))