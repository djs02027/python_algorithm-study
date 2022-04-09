def DFS(start,end):
    global flag
    queue=graph[start]

    for q in queue:
        if q==end:
            flag=1
        DFS(q,end)



T=int(input())
for i in range(1,T+1):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    for _ in range(E):
        N,M=map(int,input().split())
        graph[N].append(M)
    S,E=map(int,input().split())
    flag=0
    DFS(S,E)
    print('#{} {}'.format(i,flag))

    #
    # [[], [4, 3], [3, 5], [], [6], [], []]
    # [[], [6], [3, 6], [5], [], [], [], []]
    # [[], [5], [6, 9], [9], [7, 8], [7, 3], [], [8], [], []]
    #

