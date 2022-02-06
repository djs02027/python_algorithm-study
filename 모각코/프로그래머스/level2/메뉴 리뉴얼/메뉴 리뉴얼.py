from itertools import combinations


def solution(orders, course):
    courselist = set(orders)
    courselist = list(courselist)
    cac = {}
    for c in courselist:
        cac[c] = 0
    for o in orders:
        order = []
        for i in range(len(o)):
            order.append(o[i])
        orderlen = len(order)
        totalcombi = []
        for i in range(2, orderlen + 1):
            totalcombi = (list(combinations(order, i)))
            for t in totalcombi:
                courseone = ''.join(map(str, t))
                if courseone in courselist:
                    cac[courseone] += 1
    print(cac)
    answer = []
    for c in course:
        for k, v in cac.items():
            if v == c:
                print(k)

    answer.sort()

    return answer