N, S = map(int, input().split())
numbers = list(map(int, input().split()))
minV = int(1e9)

Lp, Rp = 0, 0
total = numbers[Lp]
while True:
    if Lp > Rp:
        break
    if total < S:
        Rp += 1
        if Rp >= N:
            break
        total += numbers[Rp]

    else:
        minV = min(minV, Rp - Lp + 1)
        total -= numbers[Lp]
        Lp += 1
        if Lp >= N:
            break

if minV == int(1e9):
    print(0)
else:
    print(minV)
