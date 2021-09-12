import sys
sys.stdin=open('input.txt')
city = int(input())
travel = [list(map(int, input().split())) for _ in range(city)]
dp = [[0] * (1 << city-1) for _ in range(city)]

def tsp(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (city-1)) - 1:
        if travel[i][0]:
            return travel[i][0]
        else:
            return float('inf')

    min_route = float('inf')

    for j in range(1, city):
        if not travel[i][j]:
            continue
        if route & (1 << j-1):
            continue
        D = travel[i][j] + tsp(j, route | (1 << (j-1)))
        if min_route > D:
            min_route = D

    dp[i][route] = min_route

    return min_route


print(tsp(0,0))

