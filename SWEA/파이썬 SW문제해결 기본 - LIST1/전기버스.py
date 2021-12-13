import sys
sys.stdin=open('전기버스.txt')
T=int(input())
for tc in range(1,T+1):
    K,N,M=map(int,input().split())
    bus_stop=list(map(int, input().split()))
    charging_place=[0]*(N+1)
    for b in bus_stop:
        charging_place[b]=1
    print(charging_place)
    charging_cnt=0
    i=0
    flag=0
    while i<len(charging_place):
        i+=K
        if flag==1 or i>=N:
            break
        if 0<=i<len(charging_place) and charging_place[i]==1:
              charging_cnt+=1
        else:
            for j in range(i,i-K,-1):
                if 0<=j<len(charging_place) and charging_place[j]==1:
                    charging_cnt+=1
                    i=j
                    break
            else:
                charging_cnt=0
                flag=1

    print("#{} {}".format(tc,charging_cnt))