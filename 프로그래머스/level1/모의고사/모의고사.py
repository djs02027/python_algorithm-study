def addlist(arr, N):
    tmp = list(arr)
    if N > len(arr):  # 패턴의 길이가 문제수보다 작을 때
        while N >= len(tmp):
            for i in arr:
                tmp.append(i)
        tmp = tmp[:N]
    else:
        tmp = arr[:N]

    return tmp


def match(arr, answers, N):
    cnt = 0
    for i in range(N):
        if arr[i] == answers[i]:
            cnt += 1
    return cnt


def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    N = len(answers)  # 문제수
    p1 = addlist(pattern1, N)
    p2 = addlist(pattern2, N)
    p3 = addlist(pattern3, N)
    resultp1 = match(p1, answers, N)
    resultp2 = match(p2, answers, N)
    resultp3 = match(p3, answers, N)
    maxvalue = max(resultp1, resultp2, resultp3)
    result = []
    if maxvalue == resultp1:
        result.append(1)
    if maxvalue == resultp2:
        result.append(2)
    if maxvalue == resultp3:
        result.append(3)

    return result