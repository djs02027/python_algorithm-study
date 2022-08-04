#https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/
def computeLPS(part, lps):
    length = 0
    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < len(part):
        if part[i] == part[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:  # 이전 인덱스에서는 같았는데 지금은 다른 경우
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                length = lps[length - 1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:  # 시작부터 다른경우
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1


def KMP(w, p):
    global match
    part_len = len(p)
    word_len = len(w)
    # 건너뛸만큼의 길이를 구함
    lps = [0] * part_len
    # 부분 탐색 문자열의 접두사와 접미사의 길이를 알아야, 그만큼 건너뛴 후에 탐색을 진행
    computeLPS(p, lps)
    i = 0
    j = 0
    while i < word_len:
        if p[j] == w[i]:
            i += 1
            j += 1
        elif p[j] != w[i]:
            if j != 0:  # 이전 인덱스에서는 같았고 현재는 다른경우
                j = lps[j - 1]
            else:
                i += 1  # 시작부터 다른경우
        if j == part_len:
            j = lps[j - 1]
            match=1


match = 0
word = input()
part = input()

KMP(word, part)
print(match)
