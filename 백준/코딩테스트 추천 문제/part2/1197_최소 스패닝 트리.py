# 신장트리
#
# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미
# 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 합니다.
#
# - 크루스칼 알고리즘
# 간선데이터를 비용에 따라 오름차순으로 정렬
# 간선을 하나씩 확인 하면서 사이클이 발생하는 지 확인하면서
# 사이클이 발생하지 않는 경우 최소신장 트리에 포함시키고 사이클에 발생하는 경우 포함시키지 않는다
# 모든 간선에 대하여 2번의 과정을 반복

def findParent(parents, x):
    if parents[x] != x:
        parents[x] = findParent(parents, parents[x])
    return parents[x]


def unionParent(parents, s, e):
    s = findParent(parents, s)
    e = findParent(parents, e)
    if s < e:
        parents[e] = s
    else:
        parents[s] = e


V, E = map(int, input().split())
graph = []
parents = [[] for _ in range(V + 1)]
for i in range(V + 1):
    parents[i] = i
for i in range(E):
    s, e, cost = map(int, input().split())
    graph.append((cost, s, e))

graph.sort()
total=0
for i in range(E):
    cost, s, e = graph[i]
    if findParent(parents,s)!=findParent(parents,e):
        unionParent(parents,s,e)
        total+=cost
print(total)