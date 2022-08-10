inputlist = list(map(str, input()))
stack = []

total = 0
tmp = 1
for i in range(len(inputlist)):
    if inputlist[i] == '(':
        tmp *= 2
        stack.append('(')
    elif inputlist[i] == '[':
        tmp *= 3
        stack.append('[')
    elif inputlist[i] == ')':
        if not stack or stack[-1] == '[':
            total = 0
            break
        if inputlist[i - 1] == '(':
            total += tmp
        stack.pop()
        tmp //= 2

    elif inputlist[i] == ']':
        if not stack or stack[-1] == '(':
            total = 0
            break
        if inputlist[i - 1] == '[':
            total += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(total)
