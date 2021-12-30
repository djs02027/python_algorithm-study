import sys

sys.stdin = open('input.txt')
M, N = map(int, input().split())
chess = [list(map(str, input())) for _ in range(M)]
wstart_checked=[]
flag = 0
ucnt = 0
uwcnt = 0
ubcnt = 0
dcnt = 0
dbcnt = 0
dwcnt = 0
for i in range(len(chess)):
    for j in range(len(chess[i])):
        if i%2==0: #홀수행
            if j%2==0:#홀수열
                print(chess[i][j],end=" ")
                ucnt+=1
                if chess[i][j]=='W':
                    uwcnt+=1
                elif chess[i][j]=='B':
                    ubcnt+=1
            else:#짝수열
                dcnt+=1
                if chess[i][j]=='W':
                    dwcnt+=1
                elif chess[i][j]=='B':
                    dbcnt+=1

        else:
            if j%2==0:#홀수열
                dcnt+=1
                if chess[i][j]=='W':
                    dwcnt+=1
                elif chess[i][j]=='B':
                    dbcnt+=1

            else:#짝수열
                print(chess[i][j],end=" ")
                ucnt+=1
                if chess[i][j]=='W':
                    uwcnt+=1
                elif chess[i][j]=='B':
                    ubcnt+=1
    print()
if uwcnt>ubcnt:
    pass
print(ucnt,uwcnt,ubcnt)
#첫행이 B일때
print(ucnt-ubcnt)
#첫행이 W일때
print(ucnt-uwcnt)


print(dcnt,dwcnt,dbcnt)

#첫행의 두번째 열이 B일때
print(dcnt-dbcnt)
#첫행의 두번째 열이 W일때
print(dcnt-dwcnt)

