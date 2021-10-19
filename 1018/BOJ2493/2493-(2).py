import sys

sys.stdin = open('input.txt')
'''
모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 
탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 
하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다. 
'''
N = int(input())
arr = list(map(int, input().split()))
tops = [0] * N

stack = []
# for i in range(len(arr)):
#     while stack:
#         if stack[-1][0] > arr[i]:
#             tops[i] = i
#             break
#         else:
#             stack.pop()
#     stack.append([arr[i], i])
# print(tops)
for i in range(len(arr)):
    while stack:
        if stack[-1][0] > arr[i]:
            tops[i] = stack[-1][1]+1
            break
        else:
            stack.pop()
    stack.append([arr[i], i])
result=' '.join(map(str,tops))
print(result)