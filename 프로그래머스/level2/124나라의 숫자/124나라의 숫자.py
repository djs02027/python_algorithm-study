def solution(n):
    # 1,4,7,10,...
    # 1,11,21,41,...
    i = 1
    answer = 0
    while n:
        cac = n % 3
        if cac == 0:
            answer += 4 * i
            n -= 1

        else:
            answer += cac * i
        n //= 3
        i *= 10

    return str(answer)