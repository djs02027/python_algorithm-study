def divide(x, y, N):
    global W, B
    divide_total = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            if paper[i][j]:
                divide_total += 1
    if not divide_total:
        W += 1
    elif divide_total == N ** 2:
        B += 1
    else:
        divide(x, y, N // 2)
        divide(x + N // 2, y, N // 2)
        divide(x, y + N // 2, N // 2)
        divide(x + N // 2, y + N // 2, N // 2)


N = int(input())
END = N
paper = [list(map(int, input().split())) for _ in range(N)]
W, B = 0, 0

divide(0, 0, N)
print(W)
print(B)