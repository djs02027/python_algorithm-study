#시간초과
import sys
sys.stdin=open('input.txt')

N,Q=map(int,input().split())
visited=[0]*(N+1)

for i in range(Q):
    duck=int(input())
    tmp=duck
    result=0
    while tmp>1:
        if visited[tmp]:
            result=tmp
        tmp //= 2
    if not result:
        visited[duck] = 1
    print(result)
