N = int(input())
result = []
for i in range(1,N):
    cac = 0
    for s in str(i):
        cac += int(s)
    tmp = i + cac
    if tmp == N:
        result.append(i)
if result:
    print(result[0])
else:
    print(0)