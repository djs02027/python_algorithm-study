from collections import deque


#인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용.
def BFS(graph, start, endPoint, visited):
    # 시작 노드를 큐에다가 먼저 삽입(삽입할 때 파이썬 리스트[]로 감싸주기)
    queue = deque([(start, 0)])
    # 시작 노드를 방문 처리


    while queue:
        v, cnt = queue.popleft()

        # 미방문시 방문으로 표시
        if not visited[v]:
            visited[v] = True
        # 방문한 노드와 연결된 노드들을 탐색
        for i in graph[v]:
            #방문되지 않은 노드이고 도착노드라면 지나간 간선 개수 +1 을 하고 결과 반환
            if not visited[i] and i == endPoint:
                return cnt + 1
            #방문하지 않은 노드이면 큐에 삽인
            elif not visited[i]:
                queue.append((i, cnt + 1))
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    Link = [[] for _ in range(V + 1)]
    for _ in range(E):
        L, R = map(int, input().split())
        Link[L].append(R)
        Link[R].append(L)
    S, G = map(int, input().split())
    visited = [False] * len(Link)

    print('#{} {}'.format(tc, BFS(Link, S, G, visited)))
