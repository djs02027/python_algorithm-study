#      1 2 3 4 5 6 7 8 9 10
#   1  1 1 1 1 1 1 1 1 1 1
#   2  0 1 1 2 2 3 3 4 4 5
#   5  0 0 0 0 1 1 2 2 3 4
#        2 2 3 4 4 6 7 8 10
N, K = map(int, input().split())
coinList = []
for _ in range(N):
    num = int(input())
    coinList.append(num)
total = [0] * (K + 1)
total[0] = 1
for c in coinList:
    for j in range(c, K + 1):
        total[j] += total[j - c]
print(total[K])
