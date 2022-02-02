
N=int(input())
text=input()
i=0
cac=0
for t in text:
    num=ord(t)-96
    cac+=num*pow(31,i)
    i+=1
print(cac%1234567891)