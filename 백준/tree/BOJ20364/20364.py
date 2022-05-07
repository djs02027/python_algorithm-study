import sys
sys.stdin=open('input.txt')


N,ducks=map(int,input().split())
duck=[]
tree={}
root=1
for i in range(ducks):
    tmp=int(input())
    duck.append(tmp)

for i in range(1,N):
    if 2*i<=N:
        tree[i]=[2*i]
    if 2*i+1<=N:
        tree[i].append(2*i+1)

print(tree)
stack=[0]
visited=[0]*(N+1)

### 시간초과..
for d in duck:
    for k,v in tree.items():
        for j in range(len(v)):
            if not visited[k] and v[j]==d:
                visited[d]=1
                print(0)
            if visited[k] and v[j]==d:
                print(k)




