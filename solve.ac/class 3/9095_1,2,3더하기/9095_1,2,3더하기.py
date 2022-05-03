from itertools import permutations
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    for i in range(1,N+1):
        print(N%i)

