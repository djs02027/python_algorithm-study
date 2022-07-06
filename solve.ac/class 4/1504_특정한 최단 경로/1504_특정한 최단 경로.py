# 반드시 A->B로 이동하는 경로가 반드시 존재할때 => 다익스트라

# 예를 들어 1에서 v1, v2를 거쳐 n으로 가는 최단경로를 구하려면
# 다익스트라 1을 수행한 뒤 1에서 v1까지의 경로를 구하고,
# 다익스트라 v1을 수행한 뒤 v1에서 v2까지의 경로를 구하고,
# 다익스트라 v2를 수행한 뒤 v2에서 n까지의 경로를 구해 셋을 더한 것이 최종 최단경로가 된다.
import heapq

INF = int(1e9)


def dikjstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cost, now = heapq.heappop(heap)
        for next, value in grape[now]:
            nextCost = value + cost
            if nextCost < distance[next]:
                distance[next] = nextCost
                heapq.heappush(heap, (nextCost, next))
    return distance


N, E = map(int, input().split())
grape = [[] for _ in range(N + 1)]
for _ in range(E):
    s, e, v = map(int, input().split())
    grape[s].append((e, v))
    # 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다
    grape[e].append((s, v))
u, v = map(int, input().split())

root = dikjstra(1)[u] + dikjstra(u)[v] + dikjstra(v)[N]
backroot = dikjstra(1)[v] + dikjstra(v)[u] + dikjstra(u)[N]
result = min(root, backroot)
print(-1 if INF <= result else result)
