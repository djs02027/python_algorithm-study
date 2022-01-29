def solution(arr, divisor):
    answer = []
    for a in arr:
        if a and a%divisor==0:
            answer.append(a)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer