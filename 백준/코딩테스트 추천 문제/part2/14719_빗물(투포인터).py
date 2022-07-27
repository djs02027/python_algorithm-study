H, W = map(int, input().split())
block = list(map(int, input().split()))
total = 0
Lp, Rp = 0, W - 1
Lmax = block[Lp]
Rmax = block[Rp]

while Lp < Rp:

    Lmax = max(Lmax, block[Lp])
    Rmax = max(Rmax, block[Rp])

    if Lmax < Rmax:
        total += Lmax - block[Lp]
        Lp += 1
    if Lmax >= Rmax:
        total += Rmax - block[Rp]
        Rp -= 1
print(total)