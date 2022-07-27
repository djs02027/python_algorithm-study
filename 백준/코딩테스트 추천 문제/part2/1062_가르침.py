def DFS(index, count):
    global result
    if count == K - 5:
        tmp = 0
        for word in words:
            flag = 1
            for w in word:
                if not Alpa[ord(w) - ord('a')]: # 해당 알파벳이 있는 지 확인하면서 없으면
                    flag = 0
                    break # 다음단어 확인
            if flag: # 해당하는 알파벳들이 모두있으면
                tmp += 1 # 단어를 배울 수있으므로 1개 추가
            result = max(tmp, result) # 단어들을 최대로 배울수 있는 수를 확인
        return
    for i in range(index, 26):
        if not Alpa[i]: # a~z까지 한단어씩 확인 체크하면서 1개부터~ K개까지 경우의 수 - 재귀
            Alpa[i] = 1
            DFS(i, count + 1)
            Alpa[i] = 0


N, K = map(int, input().split())
Alpa = [0] * 26
words = []
basic = ['a', 'n', 't', 'i', 'c']
for b in basic:
    Alpa[ord(b) - ord('a')] = 1

for _ in range(N):
    word = input()
    words.append(word)
result=0
DFS(0, 0)
if K < 5:
    print(0)
else:
    print(result)
