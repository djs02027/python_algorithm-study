import heapq, sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        cost, now = heapq.heappop(heap)
        #등록돼 있는 distance[now]가 cost(지금 거리) 보다 더 작은경우
        if cost > distance[now]:
            continue
        for next, nextCost in graph[now]:
            nextTotal = nextCost + cost
            if distance[next] > nextTotal:
                distance[next] = nextTotal
                heapq.heappush(heap, [nextTotal, next])
    return distance


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    S, E, C = map(int, input().split())
    graph[S].append((E, C))

startPoint, endPoint = map(int, input().split())
result = dijkstra(startPoint)
print(result[endPoint])
