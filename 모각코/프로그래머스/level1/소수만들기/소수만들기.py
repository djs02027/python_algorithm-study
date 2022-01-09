#시간초과

def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):

        if x % i == 0:
            return False
    return True


def solution(nums):
    N = len(nums)
    count = 0
    for i in range(1 << N):
        tmp = []
        for j in range(N + 1):
            if i & (1 << j):
                tmp.append(nums[j])
        if len(tmp) > 3 and len(tmp) <= 2:
            break
        if len(tmp) == 3:
            result = sum(tmp)
            if result <= 2:
                break
            total = isPrime(result)
            if total == True:
                count += 1

    answer = count
    return answer