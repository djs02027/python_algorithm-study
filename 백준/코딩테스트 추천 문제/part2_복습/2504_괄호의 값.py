ex = list(map(str, input()))
stack = []
tmp = 1
total = 0
for i in range(len(ex)):

    if ex[i] == '(':
        tmp *= 2
        stack.append(ex[i])
    elif ex[i] == '[':
        tmp *= 3
        stack.append(ex[i])
    elif ex[i] == ')':
        if not stack or stack[-1] != '(':
            total=0
            break
        elif ex[i - 1] == '(':
            total += tmp
        stack.pop(-1)
        tmp //= 2
    elif ex[i] == ']':
        if not stack or stack[-1] != '[':
            total=0
            break
        elif ex[i - 1] == '[':
            total += tmp
        stack.pop(-1)
        tmp //= 3
print(total)
