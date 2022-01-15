def solution(n, lost, reserve):
    checked = [0 for i in range(n + 1)]
    for l in lost:
        checked[l] = -1
    for r in reserve:
        checked[r] += 1
    print(checked)
    lost_p = 0
    reserve_p = 0
    for i in range(len(checked)):
        if checked[i] == -1:
            lost_p += 1
        if checked[i] == 1:
            reserve_p += 1

    for i in range(len(checked)):
        if checked[i] == -1:
            left = i - 1
            right = i + 1
            if right < n + 1 and left >= 0:
                if checked[right] == 1 and checked[left] == 1:
                    checked[i] = 2
    print(checked)

    for i in range(len(checked)):
        if checked[i] == -1:
            if i + 1 < n + 1:
                if checked[i + 1] == 1:
                    checked[i] += 1
                    checked[i + 1] = 0
    for i in range(len(checked) - 1, 0, -1):
        if checked[i] == -1:
            if i - 1 >= 0:
                if checked[i - 1] == 1:
                    checked[i] += 1
                    checked[i - 1] = 0

    for i in range(len(checked)):
        if checked[i] == 2:
            if i + 1 < n + 1:
                if checked[i + 1] == 1:
                    checked[i] = 0
                    checked[i + 1] = 0
    for i in range(len(checked) - 1, 0, -1):
        if checked[i] == 2:
            if i - 1 >= 0:
                if checked[i - 1] == 1:
                    checked[i] = 0
                    checked[i - 1] = 0

    print(checked)
    total = 0
    for i in range(1, len(checked)):
        if checked[i] == 0 or checked[i] == 1:
            total += 1

    answer = total
    return answer