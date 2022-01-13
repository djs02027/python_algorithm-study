from collections import deque
N=int(input())
cards=[i+1 for i in range(N)]
cards=deque(cards)
while len(cards)>1:
    cards.popleft()
    tmp=cards.popleft()
    cards.append(tmp)

print(cards[0])