from collections import deque

T = int(input())
for _ in range(T):
    origin, change = input().split()
    visited = [0] * 10000
    q = deque()

    q.append((int(origin), ""))

    while q:
        now, path = q.popleft()
        visited[now] = 1
        if now == int(change):
            print(path)
            break

        cac = (2 * now) % 10000
        if not visited[cac]:
            q.append((cac, path + "D"))
            visited[cac] = 1

        cac = (now - 1) % 10000
        if not visited[cac]:
            q.append((cac, path + "S"))
            visited[cac] = 1

        cac = ((now * 10) + (now // 1000)) % 10000
        if not visited[cac]:
            q.append((cac, path + "L"))
            visited[cac] = 1

        cac = (((now % 10) * 10000 + now) // 10) % 10000
        if not visited[cac]:
            q.append((cac, path + "R"))
            visited[cac] = 1
