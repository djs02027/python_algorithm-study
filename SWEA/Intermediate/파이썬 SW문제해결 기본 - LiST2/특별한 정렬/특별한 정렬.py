import sys

sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    M=max(arr)
    for i in range(N):
        MaxNum = -1;
        MinNum = 99999
        for j in range(i, N):
            if MaxNum < arr[j]:
                if i % 2 == 0:
                    MaxNum = arr[j]
                    tmp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = tmp

            if MinNum > arr[j]:
                if i % 2 == 1:
                    MinNum = arr[j]
                    tmp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = tmp
    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(arr[i],end=" ")
    print()