arr=list(input() for _ in range(10))
result=set()
for i in arr:
    result.add(int(i)%42)

print(result.__len__())