

T=int(input())
for i in range(1,T+1):
    TXT=input()
    stack=[]
    for t in TXT:
        if t=='(' or t=='{':
            stack.append(t)
        if t==')':
            if stack and stack[-1]=='(':
                stack.pop(-1)
            else:
                stack.append(')')
        elif t=='}':
            if stack and stack[-1]=='{':
                stack.pop(-1)
            else:
                stack.append('}')
    if stack:
        print('#{} 0'.format(i))
    else:
        print('#{} 1'.format(i))

