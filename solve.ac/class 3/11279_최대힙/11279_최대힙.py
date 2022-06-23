import heapq
import sys

input = sys.stdin.readline
N = int(input().rstrip())
largehq = []

for _ in range(N):
    num = int(input().rstrip())
    if num != 0:
        heapq.heappush(largehq, -int(num))


    if num == 0 and largehq:
        print(-heapq.heappop(largehq))

    elif num == 0 and not largehq :
        print(0)
