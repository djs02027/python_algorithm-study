import sys
input=sys.stdin.readline

N,M=map(int,input().rstrip().split())
poketmonList={}
for k in range(1,N+1):
    name=input().rstrip()
    poketmonList[str(k)]=name
    poketmonList[name]=k
print(poketmonList)
for _ in range(M):
    findPoketmon=input().rstrip()
    print(poketmonList[findPoketmon])

