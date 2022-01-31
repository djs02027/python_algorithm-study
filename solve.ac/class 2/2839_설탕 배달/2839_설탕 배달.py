N = int(input())

cac = 0
tmp = N
ctmp5=tmp//5
tmp5=tmp%5

while ctmp5>0:
    if tmp5%3==0:
        break
    if tmp5%3!=0:
        ctmp5-=1
        tmp5+=5
if tmp5%3==0:
    print(ctmp5+tmp5//3)
else:
    print(-1)
