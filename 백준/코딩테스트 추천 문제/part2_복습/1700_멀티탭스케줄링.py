def findWord(now):
    word=0
    index=-1
    for p in plug:
        if not p in items[now:]:
            return p
        if index< items[now:].index(p):
            index=items[now:].index(p)
            word=p
    return word
N, K = map(int, input().split())
items = list(map(int, input().split()))
plug = []
total=0
for i in range(len(items)):
    if len(plug)<N:
        if items[i] in plug:
            continue
        plug.append(items[i])
    if not items[i] in plug:
        nowWord=findWord(i)
        plug[plug.index(nowWord)]=items[i]
        total+=1
print(total)