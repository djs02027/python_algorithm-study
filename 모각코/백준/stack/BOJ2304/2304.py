import sys

sys.stdin = open('input.txt')

# N 개의 줄에는 각 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L
# 높이를 나타내는 정수 H
N = int(input())
field = []
for i in range(N):
    coumn = list(map(int, input().split()))
    field.append(coumn)
field = sorted(field)
start = field[0][0]
end = field[N - 1][0]
count = [0] * (end + 1)
maxv = 0
idx = 0
for i in range(N):
    if maxv < field[i][1]:
        maxv = field[i][1]
        idx = field[i][0]
for i in range(len(count)):
    for j in range(len(field)):
        if field[j][0]==i:
            count[i]=field[j][1]
tmpmx=-1
for  j in range(start,idx):
    if tmpmx <count[j]:
        tmpmx=count[j]
    else:
        count[j]=tmpmx
tmpmx=-1
for j in range(end,idx,-1):
    if tmpmx < count[j]:
        tmpmx = count[j]
    else:
        count[j] = tmpmx
total=0
total=sum(count)
print(total)