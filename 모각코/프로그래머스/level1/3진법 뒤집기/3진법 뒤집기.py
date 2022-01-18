def solution(n):
    arr = []
    while n > 0:
        arr.append(n % 3)
        n = n // 3
    arr = arr[::-1]
    print(arr)

    result = 0
    for i in range(len(arr)):
        result += (arr[i] * (3 ** i))
    print(result)
    answer = result
    return answer