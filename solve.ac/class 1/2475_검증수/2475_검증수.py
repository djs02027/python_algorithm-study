import math
numbers=input().split()
cnt=0
for n in numbers:
    cnt+=int(math.pow(int(n),2))
print(cnt%10)