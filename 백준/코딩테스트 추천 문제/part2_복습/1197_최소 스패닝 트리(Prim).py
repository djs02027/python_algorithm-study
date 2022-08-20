import heapq


import sys
input=sys.stdin.readline

def Prim(start):
    visited = [False] * (V + 1)
    heap = []
    heapq.heappush(heap, [0, start])
    cnt = 0
    answer = 0
    while cnt < V:

        weight, now = heapq.heappop(heap)
        if not visited[now]:
            visited[now] = True
            answer += weight
            cnt += 1
            for next, nextWeight in distance[now]:
                heapq.heappush(heap, [nextWeight, next])

    return answer


V, E = map(int, input().split())
distance = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    distance[A].append((B, C))
    distance[B].append((A, C))

print(Prim(1))
