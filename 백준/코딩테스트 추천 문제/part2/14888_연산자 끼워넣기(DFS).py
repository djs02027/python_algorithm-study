def dfs(i, cac):
    global minV, maxV, add, sub, mul, div
    if i == N:
        maxV = max(maxV, cac)
        minV = min(minV, cac)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, cac + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, cac - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, cac * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(cac / numbers[i]))
            div += 1


N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
minV, maxV = int(1e9),-int(1e9)
dfs(1, numbers[0])

print(maxV)
print(minV)
