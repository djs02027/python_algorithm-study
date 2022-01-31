while True:
    N=list(map(int,input()))
    if N[0]==0:
        break
    tmp = N[::-1]
    if tmp == N:
        print("yes")
    else:
        print("no")