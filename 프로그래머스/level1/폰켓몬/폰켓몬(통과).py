#  문제를 잘 읽어보면 의외로 간단히 풀린다.

def solution(nums):
    N = len(nums)
    c = int(N // 2)
    arr = list(set(nums))
    print(arr)
    if len(arr) < c:
        c = len(arr)

    answer = c
    return answer