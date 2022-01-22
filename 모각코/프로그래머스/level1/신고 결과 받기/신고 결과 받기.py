def solution(id_list, report, k):
    result = []
    cac = [[] for _ in range(len(id_list))]
    reportCount = [0] * len(id_list)

    for r in report:
        sender, accepter = r.split(' ')
        result.append([sender, accepter])

    for i in range(len(result)):
        if result[i][0] in id_list:
            idx = id_list.index(result[i][0])
            cac[idx].append(result[i][1])

    for i in range(len(cac)):
        cac[i] = list(set(cac[i]))

    for i in range(len(cac)):
        for j in range(len(cac[i])):
            if cac[i][j] in id_list:
                idx = id_list.index(cac[i][j])
                reportCount[idx] += 1

    stopId = []
    for i in range(len(reportCount)):
        if reportCount[i] >= k:
            stopId.append(id_list[i])

    total = [0] * len(id_list)
    for i in range(len(cac)):
        for j in range(len(cac[i])):
            if cac[i][j] in stopId:
                total[i] += 1

    answer = total
    return answer