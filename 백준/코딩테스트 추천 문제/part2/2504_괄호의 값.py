example = list(map(str, input()))

tmp = 1
cac = 0
stack = []

for i in range(len(example)):
    if example[i] == '(':
        stack.append(example[i])
        tmp *= 2
    elif example[i] == '[':
        stack.append(example[i])
        tmp *= 3
    elif example[i] == ')':
        if not stack or stack[-1] == '[':
            cac = 0
            break
        if example[i - 1] == '(':
            cac += tmp
        stack.pop()
        tmp //= 2

    elif example[i] == ']':
        if not stack or stack[-1] == '(':
            cac = 0
            break
        if example[i - 1] == '[':
            cac += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(cac)
