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

3 14
1 4 3 2 5 4 3 2 5 3 4 2 3 4
'''
import sys

sys.stdin = open('input.txt')
hole, used_cnt = map(int, input().split())
order = list(map(int, input().split()))
check_hole = []
cnt = 0


def check(i):
    target = 0
    idx = -1
    # 앞으로 안쓰이는 것이라면 뽑는다.
    # 콘센트 꽃힌 번호중에 제일 멀리 있는 숫자를 뽑는다!!
    # 모두 쓰이는 것이라면 가장 나중에 쓰이는 것을 뽑는다.
    for ch in check_hole:
        if ch not in order[i:]:
            return ch
        if idx < order[i:].index(ch):
            target = ch
            idx = order[i:].index(ch)

    return target


for i in range(used_cnt):
    if len(check_hole) < hole:
        if order[i] in check_hole:
            continue
        check_hole.append(order[i])

    if order[i] not in check_hole:
        check_hole[check_hole.index(check(i))] = order[i]
        cnt += 1
print(cnt)
