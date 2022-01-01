import sys
sys.stdin=open('min_max_input.txt')
T=int(input())
for tc in range(1,T+1):
    num=int(input())
    arr=list(map(int,input().split()))
    print("#{} {}".format(tc,max(arr)-min(arr)))