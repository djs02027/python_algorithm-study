def factory(N):
    global cac

    if N == 1:
        return
    else:
        cac *= N
        try:
            return factory(N - 1)
        except:
            cac=1
            return
N=int(input())
cac=1
factory(N)
print(cac)