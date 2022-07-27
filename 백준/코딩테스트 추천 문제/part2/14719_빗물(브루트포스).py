H, W = map(int, input().split())
block = list(map(int, input().split()))
result = 0
for i in range(1, W - 1):
    Lmax = -1
    Rmax = -1
    for j in range(i):
        if block[i] <= block[j]:
            Lmax = max(Lmax, block[j])
    for k in range(i + 1, W):
        if block[i] <= block[k]:
            Rmax = max(Rmax, block[k])
    if Lmax != -1 and Rmax != -1:
        minv = min(Lmax, Rmax)
        result += minv - block[i]
print(result)
