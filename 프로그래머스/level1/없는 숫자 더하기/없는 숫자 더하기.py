def solution(numbers):
    arr = [i for i in range(10)]
    sum = 0
    for i in range(10):
        if i in numbers:
            continue
        else:
            sum += i

    answer = sum
    return answer