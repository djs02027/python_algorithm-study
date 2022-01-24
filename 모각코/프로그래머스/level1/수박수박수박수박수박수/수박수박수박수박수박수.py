def solution(n):
    text = '수박'
    t = len(text)
    if n % t == 0:
        tmp = n // t
        text = text * tmp

    elif n % t == 1:
        tmp = n // t
        text = text * tmp
        text += '수'

    answer = text
    return answer