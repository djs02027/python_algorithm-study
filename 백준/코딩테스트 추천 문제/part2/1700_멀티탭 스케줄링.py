def checkIndex(i):
    target = 0
    index = -1
    for u in q: # 꽂혀있는 플러스 리스트 순회
        if u not in usingList[i:]:
            return u # 리스트에 없으면 뽑기
        if index < usingList[i:].index(u): #멀리있는 번호 인덱스 찾기
            target = u
            index = usingList[i:].index(u)
    return target

N, K = map(int, input().split())
usingList = list(map(int, input().split()))
q = []
cnt=0
for i in range(K):
    if len(q) < N :
        if usingList[i] in q:
            continue
        q.append(usingList[i])
    if  usingList[i] not in q:
        now=checkIndex(i)
        q[q.index(now)]=usingList[i] #콘센트 바꿔주기
        cnt+=1 # 뽑을때 카운트 해주기

print(cnt)