n=int(input())
divideNum=10007
prev=0
next=1
total=0
flow=0
sumN=0
while n>flow:
    sumN=prev+next
    prev=next
    next=sumN
    flow=flow+1
print(next%divideNum)
