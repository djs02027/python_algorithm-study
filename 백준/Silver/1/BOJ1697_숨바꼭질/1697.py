'''
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면
1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

'''
#시간초과

from collections import deque
import sys
sys.stdin=open('input.txt')
def flagcac(n,i):
    result={
        0: lambda n:n*2,
        1: lambda n:n-1,
        2: lambda n:n+1,
    }[i](n)
    return result

def BFS():
    global total, minv
    while q:
        num,idx=q.pop()
        if num==sister:
            total=idx
            return
        for i in range(3):
            cac=flagcac(num,i)
            if 0<=cac<=100000 and not visited[cac]:
                q.append((cac,idx+1))
                visited[cac]=1

subin,sister=map(int,input().split())
visited=[0]*100002
cnt=0
total=0

q=deque()
q.append((subin,cnt))
BFS()
print(total)