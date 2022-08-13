from collections import deque
from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))
opflag = ['+', '-', '*', '//']
tmp = []
for i in range(len(op)):
    for j in range(op[i]):
        tmp.append(opflag[i])
total = list(permutations(tmp, len(tmp)))
q = deque(total)
maxv = -int(1e9)
minv = int(1e9)
while q:
    nowlist = q.popleft()
    total = numbers[0]

    for i in range(1, len(numbers)):
        if nowlist[i - 1] == '+':
            total += numbers[i]
        elif nowlist[i - 1] == '-':
            total -= numbers[i]
        elif nowlist[i - 1] == '*':
            total *= numbers[i]
        elif nowlist[i - 1] == '//':
            if total > 0:
                total //= numbers[i]
            else:
                total = -(abs(total) // numbers[i])
    maxv = max(maxv, total)
    minv = min(minv, total)
print(maxv)
print(minv)