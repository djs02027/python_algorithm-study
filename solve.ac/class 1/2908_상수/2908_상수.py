a,b =input().split()
num1=""
for i in range(len(a)-1,-1,-1):
    num1+=a[i]
num2=""
for i in range(len(b)-1,-1,-1):
    num2+=b[i]
print(max(num1,num2))