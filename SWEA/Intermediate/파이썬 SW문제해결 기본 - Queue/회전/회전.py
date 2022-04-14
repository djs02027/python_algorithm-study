from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # print(numbers)
    q = deque(numbers)
    cnt = 0
    while True:
        if cnt == M:
            break
        Head = q.popleft()
        q.append(Head)

        cnt += 1
    print('#{} {}'.format(tc, q[0]))
