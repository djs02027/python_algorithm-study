A,B,V=map(int,input().split())
cac=0
flag=0
while cac<V:
    flag += 1
    cac+=A
    if cac==V:
        print(flag)
        break
    cac-=B

print(flag)