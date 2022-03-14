
Now=100
cnt=0
channer=input()
breakN=int(input())
if breakN:
    breakButton=list(input().split())
else:
    breakButton=[]
button=[i for i in range(10)]
op = abs(Now-int(channer))

#500000일때 + - 했을 경우 0에서 500000까지 이동범위와 1000000에서 이동범위를 갖게 조정해준다.
for i in range(1000001):
    text=str(i)
    flag=0
    for t in text:
        if t in breakButton:
            flag=1
            break
    if flag==0:

        op=min(op,abs(int(text)-int(channer))+len(text))
print(op)