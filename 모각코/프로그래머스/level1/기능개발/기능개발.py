import math


def solution(progresses, speeds):
    distribution = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = math.ceil(remain / speeds[i])
        distribution.append(day)
    print(distribution)
    cac = 1

    C = len(distribution)
    maxv = -1
    flag = 0
    total = []
    result = []
    for i in range(len(distribution)):
        if distribution[i] > maxv:
            maxv = distribution[i]
            total.append(i)
    total.append(C)
    total = total[::-1]
    for i in range(1, len(total)):
        result.append(total[i - 1] - total[i])

    answer = result[::-1]

    return answer