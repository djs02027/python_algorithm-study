import sys
sys.stdin=open('input.txt')
'''
모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 
탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 
하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다. 
'''
N=int(input())
arr=list(map(int,input().split()))
tops=[0]*N

stack=[]
# N번만큼 반복하는 이중 for문이 있으므로 위 소스의 시간 복잡도는 O(n²).
cnt=N
i=1
while cnt>0:
    cnt=N-i
    stack.append(arr[cnt])
    for j in range(cnt-1,-1,-1):
        if stack and stack[-1]<arr[j]:
            tops[cnt]=j+1
            stack.pop()
    i+=1
result=' '.join(map(str,tops))
print(result)

# N=int(input())
# arr=list(map(int,input().split()))
# tops=[0]*N
#
# stack=[]
#
# for i in range(len(arr)-1,-1,-1):
#     stack.append(arr[i])
#     for j in range(i-1,-1,-1):
#         if stack and stack[-1]<arr[j]:
#             tops[i]=j+1
#             stack.pop()
#
# result=' '.join(map(str,tops))
# print(result)