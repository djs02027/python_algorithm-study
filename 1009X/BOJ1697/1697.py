'''
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면
1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

'''
#시간초과
import sys
sys.stdin=open('input.txt')
subin,sister=map(int,input().split())
cnt=0
while True:
    if sister==subin:
        break
    if ((subin & 1)==1):
        subin=(subin<<1)
        cnt+=1
    else:
        subin-=1
        cnt+=1
print(cnt)