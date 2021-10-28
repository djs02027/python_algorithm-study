# , 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고,
# 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안
'''
순서
키보드
헤어드라이기
핸드폰 충전기
디지털 카메라 충전기
키보드
헤어드라이기
'''
# 첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)
# 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수


'''
반례 발생 

3 9
1 2 3 4 1 1 1 1 3

'''
import sys

sys.stdin = open('input.txt')
hole, used_cnt = map(int, input().split())
order = list(map(int, input().split()))

cnt = 0

while order:
    q = []
    if len(order) >= hole:
        for i in range(hole):
            tmp = order.pop(0)
            q.append(tmp)
        for i in range(hole):
            if i < len(order) and not order[i] in q:
                cnt += 1
    if len(order) < hole:
        order.clear()

print(cnt)