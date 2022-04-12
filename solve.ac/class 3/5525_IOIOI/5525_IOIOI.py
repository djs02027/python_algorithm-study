N=int(input())
M=int(input())
txt= input()
I=N+1
O=N
Total=I+O
for i in range(len(txt)):
    txt[i:i+Total].count()