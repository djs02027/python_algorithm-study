T = int(input())
for tc in range(1, T + 1):
    txt = list(input().split())
    txt.pop(-1)
    stack = []
    flag = True
    for t in txt:
        if t.isdigit():
            stack.append(int(t))
        else:

            try:
                op2 = stack.pop()
                op1 = stack.pop()


                if t == '+':
                    cac = op1 + op2
                    stack.append(cac)

                elif t == '-':

                    cac = op1 - op2
                    stack.append(cac)
                elif t == '*':

                    cac = op1 * op2
                    stack.append(cac)
                elif t == '/':

                    cac = op1 // op2
                    stack.append(cac)
            except:
                flag=False
    if flag==False or len(stack)>1:
        print('#{} error'.format(tc))
    else:
        print('#{} {}'.format(tc, stack[-1]))