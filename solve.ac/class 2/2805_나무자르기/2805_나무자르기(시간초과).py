N, M = map(int, input().split())
trees = list(map(int, input().split()))
MinTrees = min(trees)
cnt = 0
while True:
    cnt = 0
    for t in trees:
        if t >= MinTrees:
            cac = (t - MinTrees)
        else:
            cac = 0
        cnt += cac
        if cnt > M:
            break

    if cnt == M:
        break

    MinTrees += 1

print(MinTrees)
