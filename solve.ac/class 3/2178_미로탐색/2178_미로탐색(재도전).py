#DFS는 최단거리를 찾기 위해 완전 탐색을 하고 그중에서 최솟값을 구하게 되는데, 경로가 무수하게 많을 수 있어 매우 오랜 시간이 소요된다.
# 실제로 DFS로 풀이 후 제출하면 시간 초과가 난다.
#반면 BFS는 최단거리를 보장한다. 이 미로탐색 문제는 모든 경우의 수를 구하지 않고 최단거리만 구하면 되게 때문에 BFS로 풀이한다.
from collections import deque
import  sys
input = sys.stdin.readline

N,M= map(int ,input().rstrip().split())
Map = [list(map(int ,input().rstrip())) for _ in range(N)]

dr=[0,0,-1,1]
dc=[1,-1,0,0]


q=deque()
sr,sc=0,0
q.append([sr,sc])
while q:
    r,c=q.popleft()
    for i in range(4):
        cc= c+dc[i]
        rc= r+dr[i]
        if 0<=cc<M and 0<=rc<N:
            if Map[rc][cc]==1:
                Map[rc][cc]=Map[r][c]+1
                q.append([rc,cc])

print(Map[N-1][M-1])
