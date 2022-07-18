T=int(input())
for i in range(T):
    numbers=list(map(int,input().split()))
    numbers.sort()
    print(numbers[len(numbers)-3])