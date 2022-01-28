N, M = map(int, input().split())

arr = [i for i in range(1,N + 1)]
checked=[0]*N
start=M-1
for i in range(1,N):
    if checked and len(checked) >((M*i)-1):
        checked[(M*i)-1]=1
        print(arr[(M*i)-1])
        arr.pop((M*i)-1)
    else:
        if checked and len(checked) > (N-((M * i) - 1)):
            checked[N-((M * i) - 1)] = 1
            print(arr[N-((M * i) - 1)])








