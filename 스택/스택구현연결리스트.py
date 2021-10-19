
#노드 구조체 선언
class Node:
    def __init__(self, item, next):
        self.item = item # 노드의 값
        self.next = next # 다음 노드를 가르키는 포인터


class Stack:
    def __init__(self):
        self.last = None # 초기가르키는 값을 None으로 설정, 마지막 값을 가르킴

    def push(self, item):
        self.last = Node(item, self.last) # 값, 이전값을 가르키는 연결

    def pop(self):
        item = self.last.item #값
        self.last = self.last.next #이전 값과 이전 값의 연결
        return item #값 리턴

S=Stack()
for i in range(1,6):
    S.push(i)
    print(S.last.item)
for _ in range(5):
    print(S.pop())