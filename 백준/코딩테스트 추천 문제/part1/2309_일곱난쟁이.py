def DFS(depth):
    global flag
    if flag == True:
        return
    if depth == 7:
        if sum(visited) == 100:
            for v in visited:
                print(v)
            flag = True

    else:
        for i in range(depth, len(people)):
            if people[i] not in visited:
                visited.append(people[i])
                DFS(depth + 1)
                visited.pop()


N = 9
people = []
visited = []
flag = False
for _ in range(N):
    people.append(int(input()))
people.sort()
DFS(0)

