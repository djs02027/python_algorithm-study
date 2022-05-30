# 실패
import sys

sys.stdin = open('input.txt')
'''
1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다.
양수가 적혀 있을 경우에는 오른쪽으로, 
음수가 적혀 있을 때는 왼쪽으로 이동한다

풍선 속 숫자가 음수이면 인덱스에 풍선 속 숫자를 더한 후 리스트의 길이로  나눈 나머지가 다음 인덱스로 나온다
풍선 속 숫자가 양수이면 인덱스에 풍선 속 숫자에서 1을 뺀 것을 더한 후 리스트의 길이로 나눈 나머지가 다음 인덱스로 나온다.
'''
N = int(input())
balloons = list(map(int, input().split()))
list_idx = [i for i in range(1, N + 1)]
result = []
idx = 0
balloon = balloons.pop(idx)
result.append(list_idx.pop(idx))
while len(balloons) > 0:
    if balloon >= 0:
        idx = (idx + (balloon - 1)) % len(balloons)
    elif balloon < 0:
        idx = (idx + balloon) % len(balloons)

    balloon = balloons.pop(idx)
    result.append(list_idx.pop(idx))

for re in result:
    print(re, end=' ')