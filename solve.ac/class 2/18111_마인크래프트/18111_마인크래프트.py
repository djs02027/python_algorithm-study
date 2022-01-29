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
    if b < 0: # 정해진 블록의 수보다 더 필요하면 -1를 출력하도록 함
        return -1
    return time


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

total = []
for i in range(257): # 블록은 256을 초과할 수 없지만. 256의 높이가 올수 있다!!! (중요)
    t = findTime(i, arr, B)
    if t >= 0:
        total.append([t, i]) #시간과 블록의 높이를 넣는다.
total.sort(key=lambda x: x[1],reverse=True) #시간이 같은 경우 블록수 가 큰 것을 출력하도록 정렬
total.sort(key=lambda x: x[0])



print(' '.join(map(str, total[0])))
