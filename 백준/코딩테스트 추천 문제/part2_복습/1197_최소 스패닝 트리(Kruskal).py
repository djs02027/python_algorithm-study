def findParent(parents, x):
    if parents[x] != x:
        parents[x] = findParent(parents, parents[x])
    return parents[x]


def unionParent(parents, s, e):
    s = findParent(parents, s)
    e = findParent(parents, e)
    if s < e:
        parents[e] = s
    else:
        parents[s] = e


V, E = map(int, input().split())
parents = [[] for _ in range(V + 1)]
for i in range(V + 1):
    parents[i] = i
grape = []
for _ in range(E):
    s, e, w = map(int, input().split())
    grape.append((w, s, e))

grape.sort()
total = 0
for i in range(E):
    weight, s, e = grape[i]
    if findParent(parents, s) != findParent(parents, e):
        unionParent(parents, s, e)
        total += weight
print(total)
