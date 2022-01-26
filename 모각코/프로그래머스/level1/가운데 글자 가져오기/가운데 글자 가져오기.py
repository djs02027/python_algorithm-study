def solution(s):
    end = len(s)
    start = 0
    mid = (start + end) // 2
    if end % 2 != 0:
        answer = s[mid]
    else:
        answer = s[mid - 1] + s[mid]

    return answer