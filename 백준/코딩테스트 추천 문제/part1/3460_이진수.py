T = int(input())
for _ in range(T):
    N = int(input())
    result = str(bin(N))[2:][::-1]
    for r in range(len(result)):
        if result[r] == '1':
            print(r, end=" ")
