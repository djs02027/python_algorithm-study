def DFS(start):
    q=[start]
    visited=[0]*(computers+1)
    visited[start]=1
    cnt=0
    while q:
        tmp=q.pop()

        for j in range(len(adj[0])):
            if adj[tmp][j]==1 and visited[j]==0:
                visited[j]=1
                q.append(j)
                cnt+=1
    return cnt



computers=int(input())
Edge=int(input())
adj=[[0]*(computers+1) for _ in range(computers+1)]
for i in range(Edge):
    n,r=map(int,input().split())
    adj[n][r]=1
    adj[r][n]=1


start=1
result=DFS(start)
print(result)