def fibo(n):
    # n 이 0이나 1일 때는 값도 0, 1이기 때문에 그대로 반환
    # 2 이상일 때만 재귀 함수 두개로 분기해 값을 반환한다.
    return fibo(n-1) + fibo(n-2) if n >= 2 else n
N=int(input())
print(fibo(N))