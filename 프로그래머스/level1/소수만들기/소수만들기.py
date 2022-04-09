import math
from itertools import combinations


def solution(nums):
    count = 0

    combi = list(combinations(nums, 3))
    total = []
    for c in range(len(combi)):
        cac = sum(combi[c])
        total.append(cac)

    n = 10000000
    array = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    for t in total:
        if array[t] == True:
            count += 1

    answer = count

    return answer