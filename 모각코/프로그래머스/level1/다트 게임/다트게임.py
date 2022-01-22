import re


def solution(dartResult):
    arrcac = re.findall(r'\d+|[S,D,T,*,#]', dartResult)
    print(arrcac)
    cac = 0
    tmp = 0
    total = 0
    caclist = []
    for d in arrcac:
        if d.isnumeric():
            tmp = int(d)
        elif d == 'S':
            cac = (tmp ** 1)
            caclist.append(cac)
        elif d == 'D':
            cac = (tmp ** 2)
            caclist.append(cac)
        elif d == 'T':
            cac = (tmp ** 3)
            caclist.append(cac)
        elif d == '#':
            tmpcac = caclist.pop(-1)
            caclist.append((tmpcac * -1))
        elif d == '*':
            for c in range(len(caclist) - 1, len(caclist) - 3, -1):
                if 0 <= c:
                    caclist[c] *= 2

    total = (sum(caclist))
    answer = total
    return answer