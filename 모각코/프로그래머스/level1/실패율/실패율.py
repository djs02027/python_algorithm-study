def solution(N, stages):
    P = len(stages)
    check = [0 for _ in range(N + 2)]
    result = []

    for i in range(len(stages)):
        check[stages[i]] += 1

    check = check[:-1]
    for i in range(len(check)):
        sumN = check[i]
        if check[i]:
            result.append(sumN / P)
        else:
            result.append(0)
        P = P - check[i]

    result = result[0:-1]
    print(result)
    total = sorted(result, reverse=True)

    answer = []
    for i in range(len(total)):
        answer.append(result.index(total[i]))
        result[result.index(total[i])] = 1
    print(answer)

    return answer