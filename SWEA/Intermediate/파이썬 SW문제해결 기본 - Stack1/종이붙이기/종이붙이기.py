T=int(input())

def DP(N):
    if N==10:
        return 1
    elif N==20:
        return 3
    # 10일때 세로가 왔을때와 가로가 왔을때 두가지 경우가 생기므로 2를 곱한다.
    return DP(N-10)+(2*DP(N-20))

for i in range(1,T+1):
    N=int(input())
    print('#{} {}'.format(i,DP(N)))
