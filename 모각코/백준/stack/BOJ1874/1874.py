# 문제를 잘못 이해하여 접근했습니다.
import sys
sys.stdin=open('input.txt')
'''
843687521 -> [4, 3, 6, 8, 7, 5, 2, 1]
스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
물론 같은 정수가 두 번 나오는 일은 없다.
'''
N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))
arr=arr[::-1]
arr.insert(0,0)
print(arr)
stack=[]
tmp=[]
i=1
stack.append(i)
while stack:
    i+=1
    if i==N+1:
        break
    stack.append(i)
    if arr[len(stack)]!=i and arr[len(stack)]>=i:
        tmp.append(stack.pop(-1))
        print('-')
print(stack)
print(tmp)


