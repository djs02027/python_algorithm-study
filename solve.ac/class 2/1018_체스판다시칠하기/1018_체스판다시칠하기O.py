import sys

sys.stdin = open('input.txt')
M, N = map(int, input().split())
chess = [list(map(str, input())) for _ in range(M)]
chess_B=[[0]*8 for _ in range(8)]
chess_W=[[0]*8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            chess_B[i][j]='B'
            chess_W[i][j]='W'
        else:
            chess_B[i][j]='W'
            chess_W[i][j]='B'
# print(chess_B)
# print(chess_W)
result=M*N
for i in range(M-7):
    for j in range(N-7):
        chess_piece=[result[j:j+8] for result in chess[i:i+8]]

        B_cnt=0
        W_cnt=0
        for a in range(8):
            for b in range(8):
                if chess_piece[a][b]!=chess_B[a][b]:
                    B_cnt+=1
                if chess_piece[a][b]!=chess_W[a][b]:
                    W_cnt+=1

        result=min(result,B_cnt,W_cnt)


print(result)