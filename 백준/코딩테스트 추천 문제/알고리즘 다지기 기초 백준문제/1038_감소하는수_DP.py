#

# 0 1 2 3 4 5 6 7 8 9
# 1 1 1 1 1 1 1 1 1 1
# 0 1 2 3 4 5 6 7 8 9
# 0 0 1 3 6 10 15 21 28 36
# 321 320 310
# 432 431 430 421 420 410
def find(length, n):
    count,last_count=0,0
    for j in range(10):
        last_count=count
        count+=dp[length][j]
        if count >= n:
            break

    if length == 1:
        return str(j)

    return str(j) + find(length - 1, n - last_count)




N=int(input())
dp=[[0]*10 for _ in range(11)]
# 9876543210 10자리이므로 11까지..
row_count=[0]
for i in range(10):
    dp[1][i]=1
row_count.append(sum(dp[1]))

for i in range(2,11):
    for j in range(1,10):
        dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
    row_count.append(row_count[-1]+sum(dp[i]))
for i in range(1,11):
    if N+1 <= row_count[i]:
        print(find(i,N+1-row_count[i-1]))