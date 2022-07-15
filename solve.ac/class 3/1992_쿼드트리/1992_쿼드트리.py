def divide(start_row, start_col, size):
    if size == 1:
        #사이즈가 1이면 출력
        print(field[start_row][start_col], end="")
        return
    number = field[start_row][start_col]
    for i in range(start_row, start_row + size):
        for j in range(start_col, start_col + size):
            if number != field[i][j]:
                size //= 2
                print("(", end="")
                divide(start_row, start_col, size)
                divide(start_row, start_col + size, size)
                divide(start_row + size, start_col, size)
                divide(start_row + size, start_col + size, size)
                print(")", end="")
                return
    # 모두 같다면 출력
    print(field[start_row][start_col], end="")
    return


N = int(input())
field = [list(map(int, input())) for _ in range(N)]
divide(0, 0, N)
