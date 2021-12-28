import sys
sys.stdin=open('input.txt')
N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))
print_result=[]
stack=[]
num=0
cnt = 0
for i in range(len(arr)):
    while cnt<arr[i]:
        num+=1
        stack.append(num)
        print_result.append('+')
        cnt+=1
    if stack[-1]==arr[i]:
        stack.pop()
        print_result.append('-')
if stack:
    print('NO')
else:
    for i in print_result:
        print(i)

