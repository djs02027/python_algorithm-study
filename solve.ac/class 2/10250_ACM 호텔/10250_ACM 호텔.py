T = int(input())
# 2
# 6 12 10
# 30 50 72
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = ((N - 1) % H) + 1
    roomNum = ((N - 1) // H) + 1
    if roomNum < 10:
        room = str(floor) + str('0') + str(roomNum)
    else:
        room = str(floor) + str(roomNum)

    print(room)
