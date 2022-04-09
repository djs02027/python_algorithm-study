def solution(a, b):
    cac=0
    if a < b:
        for i in range(a,b+1):
            cac+=i
    else:
        for i in range(b,a+1):
            cac+=i
    answer = cac
    return answer