T=int(input())
for _ in range(1,T+1):
    k=int(input())
    n=int(input())

    #
    # 2 1,4,10
    # 1 1,3,6
    # 0 1,2,3
    cac=[0]*n
    tmp=[0]*n
    for j in range(n):
        cac[j] = (j + 1)

    flag=1
    while True:
        if flag==k:
            break
        total=0
        for i in range(n):
            total+=cac[i]
            tmp[i]=total
        cac=tmp
        flag+=1
    # print(cac)
    result=0
    for i in range(n):
        result+=cac[i]
    print(result)




