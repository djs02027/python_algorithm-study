#시간초과
import sys
sys.stdin = open('input.txt')


def DFS(i):
    global cac, cnt

    if i == testNum+1:
        return

    if L <= cac and cac <= R:
        maxv = -1
        minv = 987654321987654321
        for i in range(len(visited)):
            if visited[i] != 0 and maxv < visited[i]:
                maxv = visited[i]
            if visited[i] != 0 and minv > visited[i]:
                minv = visited[i]
        total = maxv - minv
        if total >= X:
            tmp = visited.copy()
            if not tmp in check:
                cnt += 1
                check.append(tmp)
            return

    else:
        for j in range(testNum):
            if visited[j]:
                continue
            cac += test_level[j]
            visited[j] = test_level[j]

            if L > cac and cac > R:
                continue
            DFS(i + 1)
            cac -= test_level[j]
            visited[j] = 0


testNum, L, R, X = map(int, input().split())
test_level = list(map(int, input().split()))
visited = [0] * (testNum + 1)
check = []
n = 0
cnt = 0
cac = 0
DFS(n)
print(cnt)
