from collections import Counter

def solution(participant, completion):
    cnt = Counter()
    for p in participant:
        cnt[p] += 1
    for c in completion:
        cnt[c] -= 1
    return list(x for x,y in cnt.items() if y == 1).pop();




def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1
    for c in completion:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
    return list(d.keys()).pop()


def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1
    for c in completion:
        d[c] -= 1
    return list(key for key, val in d.items() if val == 1).pop()