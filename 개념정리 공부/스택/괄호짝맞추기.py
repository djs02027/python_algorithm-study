

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('stack is empty')

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('stack is empty')

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self) == 0



def parChecker(parSeq):
    S = Stack()
    for symbol in parSeq:
        if symbol == '(': # (모양일때만 push한다.
            S.push(symbol)
        elif symbol==')':
            if not S.isEmpty():
                S.pop() # )이나오면 stack에 들어있는 (을 pop한다.
            else:
                return False

    else:
        if len(S) != 0:
            return False
        else:
            return True


parSeq = list(input())

print(parChecker(parSeq))
