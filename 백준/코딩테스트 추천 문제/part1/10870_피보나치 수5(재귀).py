def fibo(n):
    return fibo(n-1)+fibo(n-2) if n>=2 else n
N=int(input())
print(fibo(N))