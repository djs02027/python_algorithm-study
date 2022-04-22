T=int(input())
for tc in range(1,T+1):
    N,M,K=map(int,input().split())
    numbers=list(map(int, input().split()))
    step=M
    for i in range(1,K+1):
        step = M * i
        if step >= len(numbers):
            tmp = step - len(numbers)
            step = tmp
        cnt=numbers[step-1]+numbers[step]
        numbers[step:step]=[cnt]


    print(numbers)