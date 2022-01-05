import sys, heapq
sys.stdin = open('input.txt')

blue, red, n = map(int, input().split())

queue = list()
#heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
heapq.heapify(queue)
r_end = b_end = 0

for i in range(n):
    time, color, cnt = map(str, input().split())
    time = int(time)
    cnt = int(cnt)
    j = 0
    if color == 'R' and r_end > time:
        time = r_end
    elif color == 'B' and b_end > time:
        time = b_end

    while j < cnt:
        if color == 'B':
            #heapq.heappush(heap, item) : item을 heap에 추가
            heapq.heappush(queue, (time + blue * j, 'B'))

        else:
            heapq.heappush(queue, (time+ red * j, 'R'))

        j+=1

    if color == 'B':
        b_end = time + blue * j
    else:
        r_end = time + red * j

print(queue)
b = list()
r = list()
for j in range(len(queue)):
    #heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
    poped = heapq.heappop(queue)
    print(poped)
    if poped[1] == 'B':
        b.append(j+1)
    else:
        r.append(j+1)

# print(len(b))
# for a in b:
#     print(str(a)+" ", end="")
# print()
# print(len(r))
# for d in r:
#     print(str(d) + " ", end="")