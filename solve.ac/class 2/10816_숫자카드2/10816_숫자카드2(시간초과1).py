N=int(input())
cards=list(map(int,input().split()))
M=int(input())
checklist=list(map(int,input().split()))
checked=[0]*M
for c in cards:
    if c in checklist:
       idx= checklist.index(c)
       checked[idx]+=1
print(' '.join(map(str,checked)))