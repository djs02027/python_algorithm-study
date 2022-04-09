def solution(numbers, hand):
    result = []
    i = 0
    keypad = [[i] * 3 for _ in range(4)]
    cn = 0
    for i in range(4):
        for j in range(3):
            cn += 1
            keypad[i][j] = cn
    keypad[3][1] = 0

    leftx = 3;
    lefty = 0;
    rightx = 3;
    righty = 2;

    for k in numbers:
        for i in range(4):
            for j in range(3):
                if j == 0 and k == keypad[i][j]:
                    result.append('L')
                    leftx = i
                    lefty = j
                elif j == 2 and k == keypad[i][j]:
                    result.append('R')
                    rightx = i
                    righty = j
                elif j == 1 and k == keypad[i][j]:
                    nowx = i;
                    nowy = j

                    leftcnt = abs(nowx - leftx) + abs(nowy - lefty)
                    rightcnt = abs(nowx - rightx) + abs(nowy - righty)

                    if leftcnt > rightcnt:
                        result.append('R')
                        rightx = i
                        righty = j
                    elif leftcnt < rightcnt:
                        result.append('L')
                        leftx = i
                        lefty = j
                    elif leftcnt == rightcnt:
                        if hand == "left":
                            result.append('L')
                            leftx = i
                            lefty = j
                        if hand == "right":
                            result.append('R')
                            rightx = i
                            righty = j

    answer = ''.join(result)
    return answer