
def In_order(n):
    global visit
    if n:
        In_order(Left[n])
        visit.append(n)
        In_order(Right[n])


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    Left=[0]*(N+1)
    Right=[0]*(N+1)
    for i in range(N): #부모노드 반복
        #자식노드 설정
        #왼쪽노드
        if 2*i<=N:
            Left[i]=2*i
        #오른쪽노드
        if 2*i+1<=N:
            Right[i]=2*i+1
    visit = [0]
    In_order(1)

    root=0
    value=0
    for v in range(len(visit)):
        if visit[v]==1:
            root=v
        if visit[v]==N//2:
            value=v
    print('#{} {} {}'.format(tc,root,value))
