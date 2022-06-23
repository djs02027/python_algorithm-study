import sys

input = sys.stdin.readline
N = int(input())
S = set()
for _ in range(N):
    commend = input().rstrip()
    commendList = commend.split()
    if commendList[0] == 'add':
        S.add(int(commendList[1]))

    elif commendList[0] == 'check':
        if int(commendList[1]) in S:
            print(1)
        else:
            print(0)
    elif commendList[0] == 'remove':
        if int(commendList[1]) in S:
            S.remove(int(commendList[1]))
    elif commendList[0] == 'toggle':
        if int(commendList[1]) in S:
            S.remove(int(commendList[1]))
        else:
            S.add(int(commendList[1]))

    elif commendList[0] == 'all':
        S.clear()
        S = set([j for j in range(1, 21)])

    elif commendList[0] == 'empty':
        S = set()
