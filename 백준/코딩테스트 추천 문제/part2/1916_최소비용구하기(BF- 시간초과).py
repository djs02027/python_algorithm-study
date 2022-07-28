def bellmanford(start):
    distance[start] = 0
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for next, cost in graph[i]:
                if distance[i] != INF and distance[next] > distance[i] + cost:
                    distance[next] = distance[i] + cost


INF = int(1e9)
N = int(input())
M = int(input())
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    S, E, W = map(int, input().split())
    graph[S].append((E, W))
start, end = map(int, input().split())
bellmanford(start)
print(distance[end])
