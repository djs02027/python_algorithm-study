cnt = 0
totalcount = 0


def choicePhoneketmon(nums, shell, C):
    global cnt
    global totalcount
    if cnt == C:
        result = set()
        for s in range(len(shell)):
            if shell[s] == 1:
                result.add(nums[s])
        R = len(result)
        totalcount = max(totalcount, R)
        return

    for i in range(len(shell)):
        if shell[i] == 0:
            shell[i] = 1
            cnt += 1
            choicePhoneketmon(nums, shell, C)
            shell[i] = 0
            cnt -= 1


def solution(nums):
    N = len(nums)
    C = N // 2

    shell = [0] * N
    choicePhoneketmon(nums, shell, C)

    answer = totalcount
    return answer