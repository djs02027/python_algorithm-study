import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    commend = input().rstrip()
    N = int(input().rstrip())
    txt = input().rstrip()
    if txt == '[]':
        arr = []
    else:
        arr = deque(list(map(int, txt[1:-1].split(','))))
    Rcnt = 0

    for c in commend:

        if c == 'R':
            Rcnt += 1


        elif c == 'D':
            if not arr:
                print('error')
                break
            else:
                if Rcnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    else:
        if Rcnt % 2 == 0:
            # print('['+','.join(map(str,arr)+']'))
            print('[{}]'.format(','.join(map(str,arr))))
        else:
            arr.reverse()
            print('[{}]'.format(','.join(map(str, arr))))
