def LPS(p, lps):
    length = 0
    i = 1
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def KMP(w, p):
    global match
    w_len = len(w)
    p_len = len(p)
    # 접두사와 접미사의 길이 탐색
    # ABABX일 경우
    # 접두사 : A, AB, ABA, ABAB  접미사: X, BX, ABX,BABX 가 됨
    lps = [0] * p_len
    LPS(p, lps)
    print(lps)
    wi = 0
    pi = 0
    while wi < w_len:
        if p[pi]==w[wi]:
            wi+=1
            pi+=1
        elif p[pi] !=w[wi]:
            if pi!=0: #어느정도 앞에서 같았는데 중간에 다른게 나온경우
                pi=lps[pi-1] # lps로 건너뛴만큼 탐색
            else: #첫글자부터 다르므로 문자열의 인덱스를 다음으로 옮김
                wi+=1
        if pi==p_len: #전부 일치할때 부분문자열의 인덱스가 끝까지 돌때
            pi=lps[pi-1]
            match=1


word = input()
part = input()
match=0
KMP(word, part)
print(match)
