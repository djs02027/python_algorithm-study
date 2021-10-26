import sys, heapq

sys.stdin = open('input.txt')
blue, red, N = map(int, input().split())
customer = []
heapq.heapify(customer)
btime = rtime = 0
for _ in range(N):
    time, color, cnt = map(str, input().split())
    time = int(time)
    cnt = int(cnt)
    if color == 'B' and time < btime:
        time = btime
    elif color == 'R' and time < rtime:
        time = rtime

    n = 0
    while n < cnt:
        if color == 'B':
            heapq.heappush(customer, (time + blue * n, color))
        elif color == 'R':
            heapq.heappush(customer, (time + red * n, color))
        n += 1


    if color == 'B':
        btime = time + blue * n
    elif color == 'R':
        rtime = time + red * n

bluelist=[]
redlist=[]
for i in range(len(customer)):
    tmp=heapq.heappop(customer)
    if tmp[1]=='B':
        bluelist.append(i+1)
    elif tmp[1]=='R':
        redlist.append(i+1)
print(len(bluelist))
print(' '.join(map(str,bluelist)))
print(len(redlist))
print(' '.join(map(str,redlist)))