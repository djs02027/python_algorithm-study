
import heapq
import sys
input=sys.stdin.readline
hq=[]

N=int(input().rstrip())
for _ in range(N):
    inNum=int(input().rstrip())

    if inNum==0 and hq:
        fisrt=heapq.heappop(hq)
        print(fisrt)


    elif 0<inNum:
        heapq.heappush(hq, inNum)
    elif not hq:
        print(0)
