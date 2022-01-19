
N=int(input())

for i in range(N):
    stack=[]
    arr=list(input())
    # print(arr)

    for a in arr:
        if a=='(':
            stack.append(a)
        elif a==')':
            if stack and stack[-1]=='(' :
                    stack.pop()
            else:
                stack.append(a)


    if stack:
        print("NO")
    else:
        print("YES")