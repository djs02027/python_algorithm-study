N = int(input())
paper = [input().split() for _ in range(N)]
len_N=N
n1,n2,n3=-1,0,1
while True:

    if N==1:
        break
    check=paper[0][0]
    flag=False
    for i in range(N):
        for j in range(N):
            if paper[i][j]!=check:
                flag=True
    if flag==True:
        flag = False
        N = N // 3
        for i in range(0,len_N,N):
            for k in range(i,i+N):
                for j in range(i, i+N):
                    print((i,j))





