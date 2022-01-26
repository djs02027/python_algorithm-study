def solution(n):
    text = '수박'
    t = len(text)
    tmp = n // t
    text = text * tmp

    if n % t == 1:
        text += '수'

    answer = text
    return answer