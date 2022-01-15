def convertmaplist(n, arr):
    maplist = []
    for a in arr:
        tmp = []
        while a > 0:
            if a < 0:
                break
            tmp.append(a % 2)
            a //= 2
        if len(tmp) < n:
            re = n - len(tmp)
            for i in range(re):
                tmp.append(0)
        maplist.append(tmp[::-1])
    return maplist


def solution(n, arr1, arr2):
    map1 = convertmaplist(n, arr1)
    map2 = convertmaplist(n, arr2)
    combimap = [[''] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if map1[i][j] == 1 or map2[i][j] == 1:
                combimap[i][j] = '#'

    answer = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            if combimap[i][j]:
                tmp += combimap[i][j]
            else:
                tmp += ' '
        answer.append(tmp)

    return answer