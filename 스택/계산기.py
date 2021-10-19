'''
Infix to postfix
'''


class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def infix_to_postfix(infix):
    prec = {}  # 연산자 딕셔너리를 만들어서 우선순위 매기기
    prec["*"] = 3  # {'*':3} 과 같은 말
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opstack = Stack()  # 연산자를 쌓을 스택 공간을 만들어주기
    outstack = []  # postfix 결과를 쌓을 list 공간
    token_list = []
    for inf  in infix:
        token_list.append(inf)

    # 입력은 스페이스바로 하나하나 띄워서 받으니까 split()을 통해 각 인덱스에 문자 하나씩 넣기

    for token in token_list:
        if token == '(':
            opstack.push(token)

        elif token == ')':  # 오른쪽 괄호가 나타나면
            toptoken = opstack.pop()  # 맨 위에 있는 토큰을 toptoken이라 한다
            while toptoken != '(':  # 왼쪽괄호를 만나기 전까지
                outstack.append(toptoken)  # 만나는 모든 토큰을 outstack리스트에 저장한다
                toptoken = opstack.pop() # toptoken 값 바꾸기

        elif token in '+-/*^':  # 연산자를 만나면
            while (not opstack.isEmpty()) and (
                    prec[opstack.top()] >= prec[token]):  # 연산 순위와, opstack내에 무언가가 존재한다는 전제 하에
                outstack.append(opstack.pop())
            opstack.push(token)  # 연산자 우선순위에 따라 토큰 붙인다

        else:  # 피연산자는 그냥 붙이면 된다
            outstack.append(token)

    while not opstack.isEmpty():  # 연산자 스택이 빌 때까지
        outstack.append(opstack.pop())  # 연산자 다뽑아버리기
    return " ".join(outstack)  # 입력 형태랑 똑같이 만들어서 출력하기


infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)