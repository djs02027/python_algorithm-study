a=int(input())
b=int(input())
c=int(input())
result=a*b*c
result=str(result)
checked=[0]*10
for r in result:
    checked[int(r)]+=1
for i in range(len(checked)):
    print(checked[i])