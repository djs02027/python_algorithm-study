from collections import deque


def BFS(value):
    q = deque()
    q.append((value, 0))
    visited[value] = 1
    while q:
        now, cnt = q.popleft()
        flag = 1
        # 제곱수반복
        for r in result:
            # 현재값에서 제곱수를 뺀 나머지 값에 대해 q에 넣고 DFS돌림
            next = now - r

            if next > 0 and visited[next] == 0:
                print(next, now, r)
                #처음 제곱수에서 뺀 나머지값을 기억해뒀다가
                # 제곱수가 이전에 뺀 나머지보다 작아지는 경우까지 조건 분기하기 위해 기억
                if flag:
                    status = next
                    flag = 0
                #  제곱수가 이전에 뺀 나머지보다 작아지는 경우까지 조건 분기, 뺀 나머지 값이 4보다 큰경우 반복을 중단한다.
                if status > r and next >= 4:
                    print(status)
                    break
                visited[next] = 1
                #나머지 값과 횟수를 q에 넣음
                q.append((next, cnt + 1))
                print(q)
            # 제곱수가 0이면 cnt +1 해 리턴
            elif next == 0:
                return cnt + 1


N = int(input())
M = int(50000 * 0.5)
visited = [0] * (N + 1)
result = []
for i in range(M, 0, -1):
    result.append(i ** 2)

print(BFS(N))
