def DFS(step, total):
    global add, sub, mul, div, minv, maxv
    if step == N:
        maxv = max(maxv, total)
        minv = min(minv, total)
        return
    else:
        if add > 0:
            add -= 1
            DFS(step + 1, total + numbers[step])
            add += 1
        if sub > 0:
            sub -= 1
            DFS(step + 1, total - numbers[step])
            sub += 1
        if mul > 0:
            mul -= 1
            DFS(step + 1, total * numbers[step])
            mul += 1
        if div > 0:
            div -= 1
            DFS(step + 1, int(total / numbers[step]))
            div += 1


N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
minv = int(1e9)
maxv = -int(1e9)
DFS(1, numbers[0])
print(maxv)
print(minv)