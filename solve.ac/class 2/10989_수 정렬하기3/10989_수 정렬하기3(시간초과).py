import sys
N=int(sys.stdin.readline())
arr=[0]*10001
for _ in range(N):
    arr[int(sys.stdin.readline())]+=1
start=0

for a in range(len(arr)):
    if arr[a]:
        for i in range(arr[a]):
            print(a)