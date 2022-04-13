class Stack:
    def __init__(self):
        self.item = []

    def push(self, val):
        return self.item.append(val)

    def pop(self):
        try:
            return self.item.pop(-1)
        except IndexError:
            print("stack is empty")

    def top(self):
        try:
            return self.item.index(-1)
        except IndexError:
            print("stack is empty")

    def __len__(self):
        return len(self.item)

    def isempty(self):
        return len(self.item) == 0

S=Stack()
print(S.isempty())
S.push(1)
print(S.isempty())
S.pop()
S.push(2)
print(S.item)