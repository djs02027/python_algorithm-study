N,M=map(int,input().split())
poketmonList=[]
for k in range(1,N+1):
    poketmonList.append([k,input()])
print(poketmonList)
for _ in range(M):
    findPoketmon=input()
    if findPoketmon.isnumeric():
        print(poketmonList[int(findPoketmon)][1])
    else:
        result=list(filter(lambda x: poketmonList[x][1]==findPoketmon, range(len(poketmonList))))
        N=result.pop()
        print(print(poketmonList[N][0]))