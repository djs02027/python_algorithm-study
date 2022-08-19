N, S = map(int, input().split())
numbers = list(map(int, input().split()))
total = int(1e9)

LP, RP = 0, 0
sum = numbers[LP]
while True:
    if LP > RP:
        break
    if sum < S:
        RP += 1
        if RP >= N:
            break
        sum += numbers[RP]
    else:
        total = min(total, RP - LP + 1)
        sum -= numbers[LP]
        LP += 1
        if LP >= N:
            break
if total == int(1e9):
    print(0)
else:
    print(total)
