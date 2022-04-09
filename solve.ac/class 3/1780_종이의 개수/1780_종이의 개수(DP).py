def divide(row, col, N):
    global MN, PN, ZN

    for i in range(row, row + N):
        for j in range(col, col + N):
            if Paper[i][j] != Paper[row][col]:
                CN = N // 3
                divide(row, col, CN)
                divide(row, col + CN, CN)
                divide(row, col + (CN * 2), CN)

                divide(row + CN, col, CN)
                divide(row + CN, col + CN, CN)
                divide(row + CN, col + (CN * 2), CN)

                divide(row + (CN * 2), col, CN)
                divide(row + (CN * 2), col + CN, CN)
                divide(row + (CN * 2), col + (CN * 2), CN)
                return

    if Paper[row][col]==-1:
        MN+=1
    elif Paper[row][col]==0:
        ZN+=1
    elif Paper[row][col]==1:
        PN+=1
    return


N = int(input())
Paper = [list(map(int, input().split())) for _ in range(N)]

MN,PN,ZN=0,0,0
divide(0, 0, N)
print(MN)
print(ZN)
print(PN)