# -*- coding: utf-8 -*-

# 다익스트라 문제
# 1. A->B까지 가는 거리의 최단거리
# 2. 음의 간선이 없어야한다.
# 3. 매 상황 가장 비용이 적은 노드를 선택해 임의의 과정을 반복한다. -> 그리디

import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # 연결리스트 형태로 그래프 초기화

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))


def find_small_root():
    min_value = INF
    index = 0
    for i in range(1, N + 1):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for g in graph[start]:
        distance[g[0]] = g[1]
    for i in range(N - 1):
        # 현재 최단거리가 가장짧은 노드를 꺼내 방문 처리
        now = find_small_root()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + distance[j[1]]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    return distance


result = [[0] * (N + 1)]
arrXroot = dijkstra(X)
for i in range(1, N + 1):
    visited = [[False] * (N + 1)]
    distance = [[INF] * (N + 1)]
    arrAllroot = dijkstra(i)
    result[i]+=arrXroot[i]
    result[i]+=arrXroot[i]

print(min(result))