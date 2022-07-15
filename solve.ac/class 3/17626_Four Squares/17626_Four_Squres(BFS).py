from collections import deque


def BFS(value):
    q = deque()
    q.append((value, 0))
    visited[value] = 1
    while q:
        now, cnt = q.popleft()
        flag = 1
        for r in result:

            next = now - r
            # print(next, r)
            if next > 0 and visited[next] == 0:
                if flag:
                    status = next
                    flag = 0
                print(next, r, status)
                if status > r and next >= 4:
                    break
                visited[next] = 1
                q.append((next, cnt + 1))
            elif next == 0:
                return cnt + 1


N = int(input())
M = int(50000 * 0.5)
visited = [0] * (N + 1)
result = []
for i in range(M, 0, -1):
    result.append(i ** 2)

print(BFS(N))
