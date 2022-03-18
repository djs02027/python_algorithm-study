from collections import deque


def bfs(start):
    q = deque([])
    q.appendleft([start, 0])

    cnt=0
    while q:
        # print(q)
        now, cnt = q.pop()

        if now == K:

            result= cnt
            return result

        if now < 0 or now >= 100001:
            continue

        if 0<=now-1<100001 and not visited[now - 1] :
            tmp=now-1
            visited[tmp] = 1
            q.appendleft([tmp, (cnt + 1)])

        if 0<=now*2<100001 and not visited[now * 2]:
            tmp=now*2
            visited[tmp] = 1
            q.appendleft([tmp, (cnt + 1)])

        if 0<=now+1<100001 and not visited[now + 1]:
            tmp=now+1
            visited[tmp] = 1
            q.appendleft([tmp, (cnt + 1)])





N, K = map(int, input().split())
visited = [0] *100001

print(bfs(N))
