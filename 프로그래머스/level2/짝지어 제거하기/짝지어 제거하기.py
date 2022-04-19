def solution(s):
    answer = 0
    q = []
    for i in s:
        if not q:
            q.append(i)
        elif q[-1] == i:
            q.pop()
        elif q[-1] != i:
            q.append(i)

    if len(q):
        answer = 0
    else:
        answer = 1

    return answer