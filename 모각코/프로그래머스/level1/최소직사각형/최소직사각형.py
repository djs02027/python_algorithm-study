def solution(sizes):
    sizes.sort()
    Hori = []
    Verti = []
    for i in range(len(sizes)):
        if sizes[i][0] <= sizes[i][1]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
        Hori.append(sizes[i][0])
        Verti.append(sizes[i][1])

    print(sizes)
    a = max(Hori)
    b = max(Verti)
    answer = a * b
    return answer