def cutting(n, m, len_N):
    n1, n2, n3 = 0, 0, 0
    for i in range(0, n, len_N):
        for j in range(i, i + (len_N)):
            for k in range(m, m + (len_N)):
                print(j, k)
        print("---")


N = int(input())
paper = [input().split() for _ in range(N)]
len_N = N

#####
while True:
    if len_N == 3:
        break
    len_N = len_N // 3
    for i in range(0, N, len_N):
        cutting(N, i, len_N)
