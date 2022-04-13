def Merge(arr):
    global winner
    N=len(arr)
    if N<=2:
        print(arr)

        return
    mid =N//2
    Left_group=arr[mid:]
    Right_group=arr[:mid]
    Merge(Left_group)
    Merge(Right_group)

    # print(Left_group)
    # print(Right_group)



# 숫자 1은 가위, 2는 바위, 3은 보
T= int(input())
for tc in range(1,T+1):
    N=int(input())
    Case=list(map(int,input().split()))
    winner = 0
    Merge(Case)



