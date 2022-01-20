# https://m31phy.tistory.com/130 참고
def solution(numbers):
    numbers.sort()

    result = set()
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i != j:
                result.add((numbers[i] + numbers[j]))
    answer = sorted(list(result))
    return answer