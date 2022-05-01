import heapq
tc = int(input())
for idx in range(1, tc + 1):
    n = int(input())
    node = list(map(int, input().split()))
    heapq.heapify(node)
    node=[0]+ list(node)
    print(node)
    parent=n//2
    cnt=0
    while parent>0:
        cnt+=node[parent]
        parent//=2
    print('#{} {}'.format(idx, cnt))