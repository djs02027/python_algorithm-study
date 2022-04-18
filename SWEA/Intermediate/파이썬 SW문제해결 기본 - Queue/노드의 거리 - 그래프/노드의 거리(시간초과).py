# 인접리스트로 해결
def dfs(start_v, end_v, cnt):
    global result

    for i in Link[start_v]:
        if i == end_v:
            result = cnt
            return
        if not visited[i]:
            visited[i] = 1
            dfs(i, end_v, cnt + 1)



T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    Link = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        L, R = map(int, input().split())
        # print(L, R)
        Link[L].append(R)
        Link[R].append(L)
    S, G = map(int, input().split())
    # print(Link)
    result = 0
    visited[S] = 1
    dfs(S, G, 1)
    print('#{} {}'.format(tc, result))
