s=input()
stack = []
match = {
    ')': '(',
    '}': '{',
    ']': '[',

}

for char in s:
    if char not in match:
        stack.append(char)
    elif not stack or match[char] != stack.pop():
        print(False)

if len(stack) == 0:
    print(True)