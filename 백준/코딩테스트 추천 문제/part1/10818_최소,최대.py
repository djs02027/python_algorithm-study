import heapq
N=int(input())
Minnumbers=list(map(int,input().split()))
Maxnumbers=[-n for n in Minnumbers]
heapq.heapify(Minnumbers)
heapq.heapify(Maxnumbers)
print(heapq.heappop(Minnumbers), -heapq.heappop(Maxnumbers))