def solution(w, h):
    square = [[0] * w for _ in range(h)]
    dx = [0, 0, 1, 1]
    dy = [0, 1, 1, 2]
    k = 0
    for i in range(0, w, 2):
        if k * 3 <= h:
            for j in range(4):
                cx = (k * 3) + dy[j]
                cy = i + dx[j]
                if cx < (h + 1) and cy < (w + 1):
                    if not square[cx][cy]:
                        square[cx][cy] = 1

        k += 1
    cnt1 = 0
    total = w * h
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j] == 1:
                cnt1 += 1

    answer = total - cnt1
    return answer