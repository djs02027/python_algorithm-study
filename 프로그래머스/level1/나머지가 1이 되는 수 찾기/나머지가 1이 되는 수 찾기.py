def solution(n):
    for i in range(n - 1, 0, -1):
        if n % i == 1:
            result = i

    answer = result
    return answer