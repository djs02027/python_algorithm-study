def fibo(n):
    global memo

    if n == 0:
        memo[0] = 0
        return 0
    elif n == 1:
        memo[1] = 1
        return 1
    elif memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fibo(n - 1) + fibo(n - 2)

        return memo[n]


T = int(input())
for _ in range(1, T + 1):
    num = int(input())
    memo = [0] * (num+1)



    fibo(num)
    if num!=0:
        print(memo[num - 1], memo[num])
    else:
        print(1, 0)
