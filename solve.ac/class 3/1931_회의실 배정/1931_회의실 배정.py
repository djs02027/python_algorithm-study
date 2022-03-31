
# 많은 회의의 수를 알기 위해서는 빨리 끝나는 회의 순서대로 정렬을 해야 한다. 이유는 간단하다.
# 빨리 끝날수록 뒤에서 고려해볼 회의가 많기 때문이다. 빨리 시작하는 순서대로 정렬을 우선 한다면, 오히려 늦게 끝날 수 있기 때문이다.
#
#
#
# 즉 회의의 시작시간과 끝나는 시간도 같을 수 있다는 것은
#
# 2
#
# 3 3
#
# 3 3
#
# 의 input이 주어져도 output은 2가 나와야 한다는 것이다.


N=int(input())
time=[]
cnt=0
arrlist=[]
for i in range(N):
    flag=False
    s,e=map(int,input().split())
    time.append([s,e])

time.sort(key=lambda x: x[0])
# print(time)
time.sort(key=lambda x: x[1])
# print(time)
last=0
cnt=0
for i, j in time:
    if i>=last:
        cnt+=1
        last=j

print(cnt)