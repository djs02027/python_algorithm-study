

import sys
input = sys.stdin.readline


while True:

    text = input().rstrip()
    stack = []
    Flag = 1

    if text == '.':
        break

    for t in text:
        if t == '(' or t == '[':
            stack.append(t)
        elif t == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                flag = 0



        elif t == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                Flag = 0





    print("yes" if Flag and not stack else "no")



