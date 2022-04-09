import sys

input = sys.stdin.readline
N = int(input().rstrip())
floor = []
for _ in range(N):
    floor.append(int(input().rstrip()))

dp = []
if len(floor)>=3:
    # 1개씩 3칸을 연속해서 못밟으므로 전전칸 까지 값을 비교해줘야함
    dp.append(floor[0])  # 계단 0를 올라오는 경우 최대값
    dp.append(max(floor[0] + floor[1], floor[1]))  # 계단 1을 올라오는 경우 값
    dp.append(max(floor[0] + floor[2], floor[1] + floor[2]))  # 계단 2을 올라오는 경우 값
    # i번 째 계단까지의 최대 가중치 합" =
    # "case_B : i - 2번째 계단까지의 최대 가중치 합 + 현재 계단의 가중 치"와
    # "case_A : i- 3번째 계단까지의 최대 가중치 합 + i - 1번째 계단의 가중치 + 현재 계단의 가중 치" 중 더 큰 값

    # 4번째 계단 부터 계산
    if len(floor)==3:
        print(dp.pop())
    else:
        for i in range(3, N):
            dp.append(max(dp[i - 3] + floor[i - 1] + floor[i], dp[i - 2] + floor[i]))

        print(dp.pop())
else:
    cac=0
    for f in floor:
        cac+=f
    print(cac)