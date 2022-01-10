def solution(a, b):
    cac = 0
    for i in range(len(a)):
        cac += (a[i] * b[i])

    answer = cac
    return answer
