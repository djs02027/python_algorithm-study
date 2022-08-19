#시간초과
def DFS(index, total):
    global minv
    if total>=S:
        minv=min(minv,index)
        return

    for i in range(len(numbers)):
        if not visited[i]:
            visited[i]=1
            DFS(index+1, total+numbers[i])
            visited[i]=0


N,S=map(int,input().split())
minv=int(1e9)
numbers=list(map(int,input().split()))
visited=[0]*N

DFS(0,0)
print(minv)
