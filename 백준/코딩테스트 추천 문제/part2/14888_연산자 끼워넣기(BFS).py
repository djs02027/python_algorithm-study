from itertools import permutations
from collections import deque

N = int(input())
numbers = list(map(int, input().split()))
op = ['+', '-', '*', '//']
oplist = list(map(int, input().split()))
convertarr = []
for i in range(4):
    if oplist[i] == 0:
        continue
    else:
        for j in range(oplist[i]):
            convertarr.append(op[i])

op = list(permutations(convertarr, len(convertarr)))
q = deque(op)

maxvalue = -int(1e9)
minvalue = int(1e9)
while q:
    oplist = q.popleft()
    now = numbers[0]
    for i in range(1, len(numbers)):
        if oplist[i - 1] == '+':
            now += numbers[i]

        elif oplist[i - 1] == '-':
            now -= numbers[i]

        elif oplist[i - 1] == '*':
            now *= numbers[i]

        elif oplist[i - 1] == '//':
            if now < 0:
                #나누는 두 수의 부호가 같으면 몫이 양수, 다르면 몫이 음수가 된다.
                now = -(abs(now) // numbers[i])
            else:
                now = now // numbers[i]
    maxvalue = max(maxvalue, now)
    minvalue = min(minvalue, now)
print(maxvalue)
print(minvalue)
