def solution(a, b):
    calander = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, \
                10: 31, 11: 30, 12: 31}
    days = ["", "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    cac = 0
    for i in range(1, a):
        cac += calander[i]
    cac += b
    idx = (cac % 7)
    if idx <= 0:
        idx = 7 - idx
    print(idx)

    a={}

    answer = days[idx]
    return answer