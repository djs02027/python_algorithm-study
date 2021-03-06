import sys
sys.stdin=open('input.txt')
INF = int(1e9)
n,m = map(int, input().split())
start =int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph=[[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited=[False]*(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
print(graph)
def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1, n+1):
        if distance[i] <min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return  index


def dijkstra(start):
    #시작노드 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n-1):
        now=get_smallest_node()
        visited[now]=True
        for j in graph[now]:
            cost=distance[now]+j[1]

            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])