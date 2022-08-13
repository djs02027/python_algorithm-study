H, W = map(int, input().split())
block = list(map(int, input().split()))
total = 0
l, r = 0, W - 1
Lmax = block[l]
Rmax = block[r]
while l < r:
    Lmax=max(Lmax, block[l])
    Rmax=max(Rmax, block[r])

    if Lmax < Rmax:
        total += Lmax - block[l]
        l += 1
    if Lmax >= Rmax:
        total += Rmax - block[r]
        r -= 1
print(total)