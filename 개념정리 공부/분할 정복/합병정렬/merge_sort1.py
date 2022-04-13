def Merge_Sort(A):
    #오름차순 정렬
    N=len(A)

    if N<=1:
        return
    Mid= N//2
    Left_Group=A[:Mid]
    Right_Group=A[Mid:]
    Merge_Sort(Left_Group)
    Merge_Sort(Right_Group)

    Left=0
    Right=0
    Now=0
    while Left<len(Left_Group) and Right<len(Right_Group):
        if Left_Group[Left] <Right_Group[Right]:
            A[Now]=Left_Group[Left]
            Left+=1
            Now+=1
        else:
            A[Now]=Right_Group[Right]
            Right+=1
            Now+=1
    while Left <len(Left_Group):
        A[Now]=Left_Group[Left]
        Left+=1
        Now+=1

    while Right <len(Right_Group):
        A[Now]=Right_Group[Right]
        Right+=1
        Now+=1




arr = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
Merge_Sort(arr)
print(arr)
