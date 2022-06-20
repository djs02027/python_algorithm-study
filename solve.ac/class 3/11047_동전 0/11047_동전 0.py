N, K = map(int, input().split())
money = []
total = 0
for _ in range(N):
    num = int(input())
    if K >= num:
        money.append(num)

i = -1
while K:
    total = total + (K // money[i])
    K = K % money[i]
    i = i - 1
print(total)