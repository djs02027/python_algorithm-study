while True:
    A,B,C=map(int,input().split())
    arr=[A,B,C]
    arr.sort()
    if A==0 and B==0 and C==0:
        break
    if (arr[0]**2)+(arr[1]**2)==(arr[2]**2):
        print("right")
    else:
        print("wrong")
