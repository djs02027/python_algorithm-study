import sys

sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    canvers = [[0] * 10 for _ in range(10)]

    field = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        X = (field[i][2] - field[i][0])+1
        Y = (field[i][3] - field[i][1])+1
        for j in range(X):
            xc=field[i][0]+j
            for k in range(Y):
                yc=field[i][1]+k
                canvers[xc][yc]+=field[i][4]
    cnt=0
    for i in range(10):
        for j in range(10):
            if canvers[i][j]!=0 and canvers[i][j]!=1 and canvers[i][j]!=2:
                cnt+=1

    print("#{} {}".format(tc,cnt))