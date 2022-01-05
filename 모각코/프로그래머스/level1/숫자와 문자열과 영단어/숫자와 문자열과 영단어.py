def solution(s):

    convertor = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for k, v in enumerate(convertor):
        s = s.replace(v, str(k))

    answer = int(s)
    return answer
