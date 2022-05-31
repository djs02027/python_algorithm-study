N=int(input())
for _ in range(N):
    M=int(input())
    wear=dict()
    for _ in range(M):
        name,typeWare=input().split()


        if typeWare in wear.keys():
            wear[typeWare].append(name)
        else:
            wear[typeWare] = [name]
    cac=[]
    for k, v in enumerate(wear):
        num=len(wear[v])
        cac.append(num)
    result=1
    for i in cac:
        result=result*(i+1) # 입는경우의 수 추가
    print(result-1)
