def solution(s):
    i = 1
    C = (len(s) // 2) + 1

    checkedlist = []

    while True:
        if i == C:
            break
        text = s[:i]
        total = ""
        cnt = 1
        for j in range(i, len(s), i):
            sampletext = s[j:i + j]
            if text == sampletext:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                total += str(cnt) + text
                text = sampletext
                cnt = 1

        if cnt == 1:
            cnt = ""
        total += str(cnt) + text
        checkedlist.append(len(total))
        total = ""

        i += 1
    if len(s) == 1:
        return 1
    answer = min(checkedlist)
    return answer