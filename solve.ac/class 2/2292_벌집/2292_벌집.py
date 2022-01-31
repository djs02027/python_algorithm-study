#  벌집 규칙
# 1 7 19 37 61
#  6 12 18 24
N=int(input())
cac=1
total=0
for i in range(1,N):
    cac+=(6*i)
    if N<=cac:
        total=i
        break

print(total+1)
