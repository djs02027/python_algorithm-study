T=int(input())
for  i in range(1,T+1):
    txt= input()
    stack=[]
    for t in txt:
        if stack:
            if stack[-1]==t:
                stack.pop(-1)
                continue
        stack.append(t)
    print('#{} {}'.format(i, len(stack)))

