def solution(absolutes, signs):
    cac = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            cac = cac + absolutes[i]
        if signs[i] == False:
            cac = cac - absolutes[i]

    answer = cac
    return answer