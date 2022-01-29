def findTime(n, farr, b):
    time = 0
    for i in range(N):
        for j in range(M):

            if farr[i][j] < n:
                tmp = abs(farr[i][j] - n)
                b -= tmp
                time += (tmp * 1)
            if farr[i][j] > n:
                tmp = abs(farr[i][j] - n)
                b += tmp
                time += (tmp * 2)
    if b < 0:
        return -1
    return time


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

total = []
for i in range(257):
    t = findTime(i, arr, B)
    if t >= 0:
        total.append([t, i])
total.sort(key=lambda x: x[1],reverse=True)
total.sort(key=lambda x: x[0])



print(' '.join(map(str, total[0])))
