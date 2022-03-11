count = 0


def DFS(start, numbers, visited, total, target):
    global count
    if start == len(numbers):
        if total == target:
            count += 1
        return
    else:

        DFS(start + 1, numbers, visited, total + numbers[start], target)
        DFS(start + 1, numbers, visited, total - numbers[start], target)


def solution(numbers, target):
    global count
    N = len(numbers)
    total = 0
    count = 0
    visited = [0] * (N + 1)
    DFS(0, numbers, visited, total, target)

    answer = count
    return answer