import math

def find_prime(n):
    isThis = [True] * 1001
    for i in range(2, int(math.sqrt(n) + 1)):
        if isThis[i] == True:
            j = 2
            while i * j <= n:
                isThis[i * j] = False
                j += 1

    return [i for i in range(2,n+1) if isThis[i]]
N = int(input())

numbers = list(map(int, input().split()))
cnt = 0

result= find_prime(1000)
for n in numbers:
    if n in result:
        cnt+=1

print(cnt)