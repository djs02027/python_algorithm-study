# 벨만-포드 알고리즘을 이용해 해결하였다.
#
# 시간이 줄어들면서 출발 위치로 돌아오는 것 을 보고 벨만포드를 떠올리기
# 도로는 무방향이므로 양방향 간선 2개를 추가하기
# 웜홀의 가중치는 음수로 취급하기



def BellmanFord(start):
    distance[start] = 0
    for k in range(1,N+1):
        for i in range(1,N+1):
            for next, cost in graph[i]:
                # 현재 노드에 도달이 가능하면서
                # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
                if  distance[next] > distance[i] + cost:
                    distance[next] = cost + distance[i]
                    if k == N:
                        return True
    return False

INF = int(1e9)

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for _ in range(M):
        S, E, T = map(int, input().split())
        ##방향성이 없는 그래프이면 반대의 경우도 넣어야한다.
        graph[S].append((E, T))
        graph[E].append((S, T))

    for _ in range(W):
        WS, WE, WT = map(int, input().split())
        graph[WS].append((WE, -WT))


    result=BellmanFord(1)
    if result:
        print("YES")
    else:
        print("NO")