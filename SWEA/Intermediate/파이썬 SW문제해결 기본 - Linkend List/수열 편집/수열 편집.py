T=int(input())
for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    numbers=list(map(int,input().split()))

    for _ in range(M):
        txt=list(input().split())

        if txt[0]=='I':
            numbers[int(txt[1]):int(txt[1])]=[int(txt[2])]
        elif txt[0]=='D':
            numbers.pop(int(txt[1]))
        elif txt[0]=='C':
            numbers[int(txt[1])]=int(txt[2])

    try:
        print('#{} {}'.format(tc,numbers[L]))
    except:
        print('#{} -1'.format(tc))