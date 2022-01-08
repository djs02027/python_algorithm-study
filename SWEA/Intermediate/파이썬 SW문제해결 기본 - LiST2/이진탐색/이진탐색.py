import sys

sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    start = 1
    end = P
    find = -1
    Acnt = 0
    Bcnt = 0
    while find != A:

        cac = (start + end) // 2
        Acnt += 1
        if cac == A:
            break
        if cac < A:
            start = cac
        elif cac > A:
            end = cac

    start = 1
    end = P
    find = -1
    while find != B:

        cac = (start + end) // 2
        Bcnt += 1
        if cac == B:
            break
        if cac < B:
            start = cac
        elif cac > B:
            end = cac

    if Acnt < Bcnt:
        print("#{} A".format(tc))
    elif Acnt > Bcnt:
        print("#{} B".format(tc))
    else:
        print("#{} 0".format(tc))
