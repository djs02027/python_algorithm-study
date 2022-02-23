import heapq


def solution(scoville, K):
    scoville.sort()
    heapq.heapify(scoville)
    total = 0
    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1

        n1 = heapq.heappop(scoville)
        n2 = heapq.heappop(scoville)
        heapq.heappush(scoville, n1 + n2 * 2)

        total += 1

    answer = total
    return answer