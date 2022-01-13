
N1,N2=map(int,input().split())
lenN1=N1
re1=[]
for i in range(1,lenN1):
    if N1%i==0:
        re1.append(i)
re1.append(N1)
lenN2=N2
re2=[]
for i in range(1,lenN2):
    if N2%i==0:
        re2.append(i)
re2.append(N2)

tmpmax=1
for r1 in re1:
    if r1 in re2:
        if tmpmax<= r1:
            tmpmax=r1
if not N1 :
    tmpmax=N2
if not N2 :
    tmpmax=N1
print(tmpmax)


MulN1=set()
MulN2=set()
MulN1.add(lenN1)
MulN2.add(lenN2)
findMul=0
result=0
i=1

while True:
    if lenN1 == 0 or lenN2 == 0:
        break

    if MulN1 & MulN2:
        findMul=MulN1 & MulN2
        result=''.join(map(str,findMul))
        break

    i+=1
    cacN1=lenN1*i
    cacN2=lenN2*i
    MulN1.add(cacN1)
    MulN2.add(cacN2)


print(result)