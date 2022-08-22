
#https://m.blog.naver.com/ndb796/221236874984
from collections import deque


def topology_sort():
    global result
    q=deque()
    for i in range(1,N+1):
        if link[i]==0:
            q.append(i)
    while q:
        now=q.popleft()
        result.append[now]
        for st in student[now]:
            link[st]-=1
            if link[st]==0:
                q.append(st)




N, M = map(int, input().split())
student = [[] for _ in range(N + 1)]
link = [0] * (N + 1)
result = []
for _ in range(M):
    A, B = map(int, input().split())
    student[A].append(B)
    link[B] += 1

topology_sort()

