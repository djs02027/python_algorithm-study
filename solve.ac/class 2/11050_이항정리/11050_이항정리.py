import math
N,K=map(int,input().split())

b=math.factorial(N)
a=math.factorial(K)
c=math.factorial(N-K)
print(b//(a*c))
