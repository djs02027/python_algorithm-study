from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
checked = [0] * 300001
arr = list(combinations(cards, 3))
minv = 0
maxv = 0
results = []
for a in arr:
    tmp = sum(a)
    if tmp <= M:
        results.append(tmp)

results.sort()

print(results[-1])

