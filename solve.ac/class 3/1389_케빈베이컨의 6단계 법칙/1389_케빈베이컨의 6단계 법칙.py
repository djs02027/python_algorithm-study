from collections import deque
def BFS(step):
    global total
    count=0
    q=deque([step])
    visited[step]=1
    while q:
        tmp = q.popleft()

        for l in link[tmp]:
            if not visited[l]:
                visited[l]=1
                total[l] =total[tmp]+1
                q.append(l)


    return sum(total)


N, M= map(int,input().split())
link=[[] for _ in range(N+1)]

for i in range(M):
    l,r=map(int,input().split())
    link[l].append(r)
    link[r].append(l)

result=[]
for i in range(1,N+1):
    visited=[0]*(N+1)
    total=[0]*(N+1)
    cac_result=BFS(i)
    result.append( [i,cac_result])
result.sort(key=lambda x: x[1])
print(result[0][0])
