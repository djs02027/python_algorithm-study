T = int(input())

for tc in range(1,T+1):

    N,K= map(int,input().split())

    arr=list(range(1,13))
    # print(arr)
    # for n in range(1, N + 1):
    #     arr.append(n)

    result=0
    for i in range(1 << 12): #0~4095
        tmp=[]
        for j in range(13):

            if i & (1<<j):        # 1,2,4,8,16,32 ... (1,10,100,1000,10000 ....)

                tmp.append(arr[j])# [0]=1,[1]=2,[2]=3,[3]=4,[4]=5,[5]=6


        if len(tmp)==N:

            if sum(tmp)==K:
                result +=1

    print('#{} {}'.format(tc, result))