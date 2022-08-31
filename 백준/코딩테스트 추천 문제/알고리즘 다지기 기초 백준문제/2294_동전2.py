#      1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#   1  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#   5  0 0 0 0 1 2 3 4 5 2  3  4  5  6  3
#   12 0 0 0 0 0 0 0 0 0 0  0  1  2  3  4

N, K = map(int, input().split())
coinList = []
for _ in range(N):
    n = int(input())
    coinList.append(n)

dp=[10001]*(K+1)
dp[0]=0
for c in coinList:
    for j in range(c,K+1):
        dp[j]=min(dp[j],dp[j-c]+1)

if dp[K]==10001:
    print(-1)
else:
    print(dp[K])