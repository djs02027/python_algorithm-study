
T=int(input())
for tc in range(1,T+1):
    txt=list(input().split())
    stack=[]
    flag=0
    for t in txt:
        if t.isnumeric():
            stack.append(int(t))
        else:
            if t=='+':
                if stack:
                    op1=stack.pop()
                else:
                    flag = 1
                    break
                if stack:
                    op2=stack.pop()
                else:
                    flag = 1
                    break
                cac=op1+op2
                stack.append(cac)

            elif t=='-':
                if stack:
                    op1 = stack.pop()
                else:
                    flag = 1
                    break
                if stack:
                    op2 = stack.pop()
                else:
                    flag = 1
                    break
                cac=op1-op2
                stack.append(cac)
            elif t=='*':
                if stack:
                    op1 = stack.pop()
                else:
                    flag = 1
                    break
                if stack:
                    op2 = stack.pop()
                else:
                    flag = 1
                    break
                cac=op1*op2
                stack.append(cac)
            elif t=='/':
                if stack:
                    op1 = stack.pop()
                else:
                    flag = 1
                    break
                if stack:
                    op2 = stack.pop()
                else:
                    flag = 1
                    break
                cac=op1//op2
                stack.append(cac)
            elif t=='.':
                print('#{} {}'.format(tc, stack[-1]))
    if flag == 1:
        print('#{} {}'.format(tc, 'error'))