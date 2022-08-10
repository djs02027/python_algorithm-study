from itertools import permutations
from collections import deque

N = int(input())
numbers = list(map(int, input().split()))
op = ['+', '-', '*', '//']
oplist = list(map(int, input().split()))
op_result = []
for i in range(4):
    if oplist[i] == 0:
        continue

    for j in range(oplist[i]):
        op_result.append(op[i])


oplist = list(permutations(op_result, len(op_result)))
q = deque(oplist)
maxv=-int(1e9)
minv=int(1e9)
while q:
    now = q.popleft()
    total = numbers[0]
    for i in range(1, len(numbers)):
        if now[i - 1] == '+':
            total += numbers[i]
        elif now[i - 1] == '-':
            total -= numbers[i]
        elif now[i - 1] == '*':
            total *= numbers[i]
        elif now[i - 1] == '//':
            if total<0:
                total=-(abs(total)//numbers[i])
            else:
                total //= numbers[i]
    maxv=max(maxv,total)
    minv=min(minv,total)
print(maxv)
print(minv)