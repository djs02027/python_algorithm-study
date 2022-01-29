# 데크로 푼다.
N, M = map(int, input().split())

arr = [i for i in range(1,N + 1)]


total=[]
i=0
while i<N:
    step = 0
    while True:

        if step==(M-1):
            break
        tmp=arr.pop(0)
        arr.append(tmp)
        step+=1
    result=arr.pop(0)
    total.append(result)
    i+=1

change=', '.join(map(str,total))
print("<{}>".format(change))




