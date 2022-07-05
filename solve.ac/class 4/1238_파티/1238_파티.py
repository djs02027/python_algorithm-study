import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))


def dikjstra(start):
    distance = [INF] * (N + 1)
    heap = []
    heapq.heappush(heap,[0,start])
    distance[start]=0
    while heap:
        cost,now= heapq.heappop(heap)
        for next, nextCost in graph[now]:

            cacCost=cost+nextCost
            if cacCost < distance[next]: # next 경로까지 거리가 낮은 값을 찾아서 힙큐에 넣음
                heapq.heappush(heap,[cacCost,next])
                distance[next]=cacCost #낮은값을 넣기

    return distance
result = [0] * (N + 1)
for i in range(1, N + 1):
    root=dikjstra(i)
    backroot=dikjstra(X)
    result[i]=root[X]+backroot[i]
print(max(result))
