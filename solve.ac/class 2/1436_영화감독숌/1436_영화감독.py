N=int(input())
result=[]
for i in range(1000*N):
    if str(i).find('666')>-1:
        result.append(i)

print(result[N-1])