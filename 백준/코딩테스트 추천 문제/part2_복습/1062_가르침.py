def word_count(depth, now):
    global total
    if now == K - 5:
        tmp = 0
        for word in wordList:
            flag = 0
            for w in word:
                if not checked[ord(w) - ord('a')]:
                    flag = 1
                    break
            if not flag:
                tmp += 1
            total = max(total, tmp)
        return
    for i in range(depth, 26): # 방문처리한 이후 알파벳부터 체크함으로서 시간초과를 방지
        if not checked[i]:
            checked[i] = 1
            word_count(i, now + 1)
            checked[i] = 0


import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
# a n t i c -> 5개는 알아야함..
knownWords = ["a", "n", "t", "i", "c"]
wordList = []
total = -1
for _ in range(N):
    word = input().rstrip()
    wordList.append(word)

checked = [0] * 26
for k in knownWords:
    checked[ord(k) - ord('a')] = 1

if K < 5:
    total = 0
else:
    word_count(0, 0)
print(total)
