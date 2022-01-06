import sys
from itertools import combinations
sys.stdin=open('sample_input.txt')
#조합

T = int(input())

for tc in range(1,T+1):

    N,K= map(int,input().split())
    num=list(range(1,K+1))
    # print(num)
    count=0
    for i in range(1, N + 1):
        per = combinations(num, i)

        for j in list(per):
            tmp=list(j)
            if len(tmp)==N and sum(j) == K:
                count += 1
    print('#{} {}'.format(tc,count))