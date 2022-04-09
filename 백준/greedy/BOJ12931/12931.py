import sys

sys.stdin = open('input.txt')

N = int(input())
B = list(map(int, input().split()))

cnt = 0
while True:
    zro=True
    flag = False
    stopflag=0
    for i in range(N):
        if B[i] == 0:
            stopflag+=1
        if B[i] > 0 and B[i] % 2 == 1:
            B[i] -= 1
            cnt += 1
        if B[i] > 0 and B[i] % 2 == 0:

            flag = True
    if stopflag==N:
        break
    if flag==True:
        for i in range(N):
            B[i] //= 2
        cnt += 1

print(cnt)