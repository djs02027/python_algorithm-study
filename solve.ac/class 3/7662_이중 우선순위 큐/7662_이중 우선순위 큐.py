import heapq
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    isNum = [0] * N
    min_hq = []
    max_hq = []
    flag = 0
    for i in range(N):
        alpa, num = input().split()

        if alpa == 'I':
            heapq.heappush(min_hq, (int(num), i))  # 최소
            heapq.heappush(max_hq, (-int(num), i))  # 최대
            isNum[i] = 1  
        elif alpa == 'D':
            if int(num) == -1:
                while min_hq and isNum[min_hq[0][1]] == 0:
                    heapq.heappop(min_hq)
                if min_hq:
                    isNum[min_hq[0][1]] = 0
                    heapq.heappop(min_hq)
            elif int(num) == 1:
                while max_hq and isNum[max_hq[0][1]] == 0:
                    heapq.heappop(max_hq)
                if max_hq:
                    isNum[max_hq[0][1]] = 0
                    heapq.heappop(max_hq)

    if 1 not in isNum:
        print("EMPTY")
    else:
        while max_hq and isNum[max_hq[0][1]] == 0:
            heapq.heappop(max_hq)
        while min_hq and isNum[min_hq[0][1]] == 0:
            heapq.heappop(min_hq)
        print(-max_hq[0][0], min_hq[0][0])

