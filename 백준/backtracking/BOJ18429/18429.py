import sys

sys.stdin = open('input.txt')


def DFS(d):
    global nowW, cnt
    if d == N:
        if nowW >= 500:
            cnt += 1
        return
    if nowW < 500:
        return
    else:
        for i in range(N):
            if not visited[i]:
                nowW += kits[i]-K
                visited[i] = 1
                DFS(d + 1)
                nowW -= kits[i]-K
                visited[i] = 0


N, K = map(int, input().split())
kits = list(map(int, input().split()))
visited = [0] * N
nowW = 500
''''
대학원생은 운동 기간동안 항상 중량이 500 이상으로 유지가 되도록
N일간의 운동 플랜을 세우고자 한다. 1일차부터 N일차까지의 모든 기간동안, 
어떤 시점에서라도 중량이 500보다 작아지지 않도록 해야 한다.
현재 3대 운동 중량 500의 괴력을 소유
3일 동안 3개의 운동 키트를 사용하는 경우 운동기간동안 항상 중량이 500이상이 되도록
BFS로 푼다
'''
day = 1
cnt = 0
DFS(day)
print(cnt)
