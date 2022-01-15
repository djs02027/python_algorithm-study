def solution(N, stages):
    P = len(stages)
    result = []
    for i in range(1, N + 1):
        clearStep = stages.count(i)
        if clearStep != 0:
            result.append(clearStep / P)
        else:
            result.append(0)
        P = P - clearStep

    changeresult = []
    for k, v in enumerate(result):
        changeresult.append([v, k])
    print(changeresult)
    changeresult = sorted(changeresult, reverse=True)
    for i in range(N):
        for j in range(i, N):
            if changeresult[i][0] == changeresult[j][0]:
                tmp = changeresult[i]
                changeresult[i] = changeresult[j]
                changeresult[j] = tmp
    answer = []
    for i in range(N):
        answer.append(changeresult[i][1] + 1)

    return answer