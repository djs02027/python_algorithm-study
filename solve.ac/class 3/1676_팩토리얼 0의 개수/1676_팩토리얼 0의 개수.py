import math
import sys
input=sys.stdin.readline
N=int(input().rstrip())
result=math.factorial(N)
result=str(result)

cnt=0
for i in range(len(result)-1,-1,-1):
    if result[i]=="0":
        cnt+=1
    else:
        break
print(cnt)