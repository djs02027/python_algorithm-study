def findSum():

    rowMax = -int(1e9)
    colMax = -int(1e9)
    for i in range(N):
        row_cnt = 1
        col_cnt = 1
        for j in range(N - 1):
            if arr[i][j] == arr[i][j + 1]:
                row_cnt += 1
            else:
                row_cnt = 1

            if arr[j][i] == arr[j + 1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            rowMax=max(rowMax,row_cnt)
            colMax=max(colMax,col_cnt)

    result=max(rowMax,colMax)
    return result

N = int(input())
arr = [list(input()) for _ in range(N)]
# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]
total=0
for i in range(N):
    for j in range(N):
        now = arr[i][j]
        for k in range(4):
            cc = i + dc[k]
            cr = j + dr[k]
            if 0 <= cc < N and 0 <= cr < N:
                if arr[cc][cr] != arr[i][j]:
                    arr[cc][cr], arr[i][j] = arr[i][j], arr[cc][cr]
                    total=max(total,findSum())
                    arr[i][j], arr[cc][cr] = arr[cc][cr], arr[i][j]

print(total)