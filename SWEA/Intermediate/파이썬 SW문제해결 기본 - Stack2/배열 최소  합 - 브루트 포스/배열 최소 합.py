def Find_Min_Value(idx, visited, cac):
    global MinV
    if idx == N:
        if MinV > cac:
            MinV = cac
        return
    if cac > MinV:
        return

    for i in range(0, N):
        if visited[i] == 0:
            visited[i] = 1
            cac += Field[idx][i]
            Find_Min_Value(idx + 1, visited, cac)
            visited[i] = 0
            cac -= Field[idx][i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Field = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    cac = 0
    MinV = 99999999
    Find_Min_Value(0, visited, cac)
    print('#{} {}'.format(tc, MinV))
