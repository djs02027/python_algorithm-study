T=int(input())
for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)
    for _ in range(M):
        idx,value=map(int,input().split())
        tree[idx]=value


    for i in range(len(tree)-1,-1,-1):
        tree[i//2]+=tree[i]
    print('#{} {}'.format(tc,tree[L]))