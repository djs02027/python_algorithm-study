import sys
sys.stdin=open('구간합.txt')
T= int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=list(map(int,input().split()))
    result=[]
    for i in range(len(arr)-M+1):
        result.append(sum(arr[i:i+M]))
    print("#{} {}".format(tc,max(result)-min(result)))