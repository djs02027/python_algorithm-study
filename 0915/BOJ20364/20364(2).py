## 시간초과의 원인을 발견하고 검색해서 문제를 풀었다..

import sys
sys.stdin=open('input.txt')
N, Q = map(int, input().split())
ducks = [int(input())for _ in range(Q)]

#셋으로 중복된 값을 제거
visited = set()

for i in range(Q): #{3}, {3,5}, {3,5,6}, {2,3,5,6}
    result = 0
    duck = ducks[i]
    while duck > 1:
        if duck in visited: # 부모노드가 방문한 노드이면 부모노드번호를 result에 저장
            result = duck
        duck //= 2 # 이진 트리에서 노드 n의 부모노드 인덱스 = n/2

    visited.add(ducks[i]) 
    print(visited)

    print(result)