text=input().upper()
tmp=set(text)

result=[]
for k in tmp:
     result.append([k,text.count(k)])
# print(result)
maxvalue=-1

for i in result:
    if i[1]>maxvalue:
        maxvalue=i[1]
        maxv=i
cnt=0

for i in result:
    if maxv[1]==i[1] and maxv[1]!=1:
        cnt+=1

if cnt>=2:
    print('?')
else:
    print(maxv[0])