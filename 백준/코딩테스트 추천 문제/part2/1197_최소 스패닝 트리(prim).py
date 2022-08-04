# 메모리 초과
# 최악의 경우 빅오제곱시간이므로..

def Prim(x):
    global V, adj
    visited_set = set()
    visited_set.add(x)
    distance = 0
    for _ in range(V - 1):
        min_dist, next_node = int(1e9), -1
        for node in visited_set:
            for j in range(1, V + 1):
                if j not in visited_set and 0 < adj[node][j] < min_dist:
                    min_dist = adj[node][j]
                    next_node = j
        distance += min_dist
        visited_set.add(next_node)

    return distance


V, E = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    start, end, cost = map(int, input().split())
    adj[start][end] = cost
    adj[end][start] = cost
print(Prim(1))
