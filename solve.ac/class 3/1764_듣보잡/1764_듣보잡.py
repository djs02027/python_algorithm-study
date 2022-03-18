import sys
input=sys.stdin.readline
N, M= map(int, input().rstrip().split())
nothearing=set()
notseeing=set()
for _ in range(N):
    nothearing.add(input().rstrip())
for _  in range(M):
    notseeing.add((input().rstrip()))



arr=notseeing.intersection(nothearing)
arr=list(arr)
arr=sorted(arr)
print(len(arr))
for a in arr:
    print(a)