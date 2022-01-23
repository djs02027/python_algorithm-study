n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
targets = list(map(int, input().split()))

check={}
for c in cards:
    if c in check:
        check[c]+=1
    else:
        check[c]=1

result=[]
for t in targets:
    if t in check.keys():
        result.append(check[t])
    else:
        result.append(0)

print(' '.join(map(str,result)))