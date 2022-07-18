N,M=map(int,input().split())
GCD = 0 # 최대 공약수
LCM = 0 # 최소 공배수
for i in range(min(N, M), 0, -1):
    if N % i == 0 and M % i == 0:
        GCD = i
        break
for i in range(max(N, M), (N * M) + 1):
    if i % N == 0 and i % M == 0:
        LCM = i
        break
print(GCD)
print(LCM)