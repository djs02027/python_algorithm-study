import heapq
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    q = []
    flag=0
    for _ in range(N):
        alpa, num = input().split()
        try:
            if alpa == 'I':
                heapq.heappush(q,int(num))
            elif alpa == 'D':
                if int(num) == -1:
                    heapq.heappop(q)
                elif int(num) == 1:
                    q=heapq.nlargest(len(q),q)[1:]
                    heapq.heapify(q)

        except:
            flag=1
            print("EMPTY")

    if flag==0:
        if q:
            print(q[-1],q[0])
        else:
            print("EMPTY")
