from collections import deque

N, M = map(int, input().split())
field = [0] * 101
visited = [0] * 101
for _ in range(N):
    place, move = map(int, input().split())
    field[place] = move

for _ in range(M):
    place, move = map(int, input().split())
    field[place] = move

q = deque()
q.append(1)
visited[1] = 1
while q:
    number = q.popleft()
    if visited[100]:
        break
    for i in range(1, 7):
        next = number + i
        if 0 <= next < len(field) and field[next]:
            next = field[next]
        if 0 <= next < len(field) and visited[next] == 0:
            q.append(next)
            visited[next] = visited[number] + 1
print(visited[100]-1)
