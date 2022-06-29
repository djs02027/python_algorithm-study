def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b, trueStory):
    a = find(parent, a)
    b = find(parent, b)

    if a in trueStory and b in trueStory:
        return

    if a in trueStory:  # 진실을 아는 리스트에 있으면 그것을 부모로 적용
        parent[b] = a
    elif b in trueStory:
        parent[a] = b
    else:
        if a < b: #작은수를 부모로..
            parent[b]=a
        else:
            parent[a]=b

total=0
paricipantList = []
N, M = map(int, input().split())
trueStory = list(map(int, input().split()))[1:]
parent = list(range(N + 1))


for _ in range(M):  # 파티의 수 M
    paricipantInfo = list(map(int, input().split()))
    paricipantNum = paricipantInfo[0]
    paricipants = paricipantInfo[1:]

    for i in range(paricipantNum - 1):
        union(parent, paricipants[i], paricipants[i + 1], trueStory)

    paricipantList.append(paricipants)

for p in paricipantList:
    for i in range(len(p)):
        if find(parent, p[i]) in trueStory:
            break
    else:
        total+=1
print(total)