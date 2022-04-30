# 오른쪽 왼쪽 구분 안하고 넣기
# T=int(input())
# for tc in range(1,T+1):
#     E,N=map(int,input().split())
#     Tree=[[] for _ in range(E+2)]
#     arr=list(map(int,input().split()))
#     for i in range(0,E):
#         Tree[arr[i*2]].append(arr[(i*2)+1])
#     print(Tree)

# 오른쪽 왼쪽 구분 하고 넣기

def Pre_order(n):
    global cnt
    if n:
        cnt += 1
        Pre_order(Left[n])
        Pre_order(Right[n])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    Left = [0] * (E + 2)
    Right = [0] * (E + 2)
    arr = list(map(int, input().split()))
    for i in range(0, E):
        if not Left[arr[i * 2]]:
            Left[arr[i * 2]]=(arr[(i * 2) + 1])
        else:
            Right[arr[i * 2]]=(arr[(i * 2) + 1])
    # print(Left)
    # print(Right)
    cnt = 0
    Pre_order(N)
    print('#{} {}'.format(tc, cnt))
