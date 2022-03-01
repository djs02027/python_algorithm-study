from collections import deque
def DFS(V):
    global DFS_result
    DFS_result.append(V)
    if arr[V]:
        for a in arr[V]:
            if not DFS_visited[a]:
                DFS_visited[a]=1
                DFS(a)

def BFS(V):
    q= deque([V])
    BFS_visited[V]=1
    while q:
        V=q.popleft()
        BFS_result.append(V)
        for a in arr[V]:
            if not BFS_visited[a]:
                BFS_visited[a] = 1
                q.append(a)



N,M,V=map(int,input().split())

L=[]
R=[]

#깊은 복사가 되어서 배열 전체 값이 같게된다.
# visited=[[0]]*M
#다음과 같이 해결하여 for문을 사용해준다.
DFS_result=[]
BFS_result=[]
arr= [[] for i in range(N+1)]
DFS_visited=[0]*(N+1)
BFS_visited=[0]*(N+1)
for _ in range(M):
    l,r=map(int,input().split())
    arr[l].append(r)
    arr[r].append(l)
for i in range(len(arr)):
    arr[i].sort()

DFS_visited[V]=1
DFS(V)
print(' '.join(map(str,DFS_result)))
BFS(V)
print(' '.join(map(str,BFS_result)))