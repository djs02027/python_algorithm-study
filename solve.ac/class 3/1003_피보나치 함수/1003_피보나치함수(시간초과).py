import sys
def fibonacci(n):
    global zero
    global one
    if n == 0:
        zero+=1
        return 0
    elif n == 1:
        one+=1
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
T=int(input())
for _ in range(1,T+1):
    zero=0
    one=0
    Num=int(sys.stdin.readline())
    fibonacci(Num)
    print(zero, one)