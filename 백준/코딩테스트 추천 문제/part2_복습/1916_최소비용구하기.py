import heapq


def dijkstra(start):
    checked = [int(1e9)] * (N + 1)
    checked[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        cost, now = heapq.heappop(heap) #거리가 짧은 정점을 확정시켜준다.
        # 현재 정점보다 총 비용이 크면 continue
        # 현재의 확정되어진 정점비용이 현재 거리합비용보다 작다면 무시
        if cost > checked[now]:
            continue
        # 다음 정점과 다음정점의 비용
        for next, nextCost in city[now]:
            #현재 정점의 비용과 다음정점의 비용계산
            sumCost = cost + nextCost
            #다음 정점의 비용이 계산된 비용보다 크다면 계산된 비용으로 바꿔줌
            if checked[next] > sumCost: #다음 정점의 비용보다 비용이 작으면 바꿔줌
                checked[next] = sumCost
                heapq.heappush(heap, [sumCost, next]) #확정시켜줌
    return checked


N = int(input())
M = int(input())
city = [[] for _ in range(N + 1)]

for _ in range(M):
    sc, ec, cost = map(int, input().split())
    city[sc].append((ec, cost))


S, E = map(int, input().split())
result=dijkstra(S)
print(result[E])