def solution(d, budget):
    N = len(d)
    total = []
    cac = 0
    d.sort()
    tmp = 0
    print(d)
    for i in d:
        cac += i
        if cac <= budget:
            tmp += 1

    answer = tmp
    return answer