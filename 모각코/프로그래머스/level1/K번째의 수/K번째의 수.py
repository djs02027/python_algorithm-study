def solution(array, commands):
    answer = []
    tmp = list(array)
    for c in commands:
        result = tmp[c[0] - 1:c[1]]
        result.sort()
        answer.append(result[c[2] - 1])

    return answer