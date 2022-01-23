

N = int(input())
command = []
for i in range(N):
    text = input()
    if text.__contains__('push'):
        massage, num = text.split(' ')
        command.append([massage, num])
    else:
        command.append([text])
stack = []
for c in command:
    if c[0] == 'push':
        stack.append(c[1])
    elif  c[0] == 'pop':
        if stack:
            tmp = stack.pop(-1)
            print(tmp)
        else:
            print(-1)

    elif c[0] == 'size':
        tmp = len(stack)
        print(tmp)
    elif c[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif  c[0] == 'top':
        if stack:
            tmp = stack[-1]
            print(tmp)
        else:
            print(-1)
