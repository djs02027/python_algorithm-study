def whoWin(p_1, p_2):
    if (Case[p_1 - 1] == 1 and Case[p_2 - 1] == 3) or (Case[p_1 - 1] == 1 and Case[p_2 - 1] == 1):
        return p_1


    elif (Case[p_1 - 1] == 2 and Case[p_2 - 1] == 1) or (Case[p_1 - 1] == 2 and Case[p_2 - 1] == 2):
        return p_1

    elif (Case[p_1 - 1] == 3 and Case[p_2 - 1] == 2) or (Case[p_1 - 1] == 3 and Case[p_2 - 1] == 3):
        return p_1

    return p_2


def Merge(s, e):
    # print(s, e)
    # 대결할 사람 없으면(한 명일 때) 현재 인덱스(s) 반환
    if s == e:
        return s

    p1 = Merge(s, (s + e) // 2)
    p2 = Merge((s + e) // 2 + 1, e)
    # 0,1
    return whoWin(p1, p2)


# 숫자 1은 가위, 2는 바위, 3은 보
# 4
# 1 3 2 1
# 0 4
# 0 2
# 0 1
# 0 0
# 1 1
# 2 2
# 3 4
# 3 3
# 4 4
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Case = list(map(int, input().split()))
    start = 1
    end = N
    print('#{} {}'.format(tc ,Merge(start, end)))
