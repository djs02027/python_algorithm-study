def square(row_start, row_end, col_start, col_end, num):
    row_mid = (row_start + row_end) // 2
    col_mid = (col_start + col_end) // 2
    if r == row_start and c == col_start:
        print(num)
        return
    N = (row_mid - row_start) * (col_mid - col_start)
    if row_start <= r < row_mid and col_start <= c < col_mid:
        square(row_start, row_mid, col_start, col_mid, num)
    elif row_start <= r < row_mid and col_mid <= c < col_end:
        square(row_start, row_mid, col_mid, col_end, num + N)
    elif row_mid <= r < row_end and col_start <= c < col_mid:
        square(row_mid, row_end, col_start, col_mid, num + (N * 2))
    elif row_mid <= r < row_end and col_mid <= c < col_end:
        square(row_mid, row_end, col_mid, col_end, num + (N * 3))


N, r, c = map(int, input().split())
row_start = 0
row_end = (2 ** N)
col_start = 0
col_end = (2 ** N)
square(row_start, row_end, col_start, col_end, 0)
# 재귀함수를 이용해 영역을 4등분으로 나눠가면서 탐색할 영역 시작 좌표,
# 영역길이, 시작인텓스를 넘겨주면 된다.
