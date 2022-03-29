# import heapq
# hq=[]
# print(hq)
# N=int(input())
# for _ in range(N):
#     heapq.heappush(hq, int(input()))
# print(hq)
# while hq:
#     min_num=hq[0]
#     print(min_num)
#     while True:
#         if hq[0]!=min_num:
#             break
#         heapq.heappop(hq)

#
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
