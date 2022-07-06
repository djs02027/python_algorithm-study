import heapq

INF = int(1e9)


def dikjstra(start):
    distance = [INF] * (V + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        cost, now = heapq.heappop(heap)
        for next, value in graph[now]:
            nextCost = cost + value
            if nextCost < distance[next]:
                distance[next] = nextCost
                heapq.heappush(heap, [nextCost, next])
    return distance

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
result=dikjstra(K)
for i in range(1, len(result)):
    if result[i]==INF:
        print("INF")
    else:
        print(result[i])