from itertools import combinations


def solution(orders, course):
    answer = []

    for k in course:
        cnt = {}
        for o in orders:
            #sorted를 통해서 WX, XW가 같은 것으로 인식되게끔 정렬을 해줘야함!! -> 핵심
            result = list(combinations(sorted(o), k))
            for r in result:
                txt = ''.join(map(str, r))

                if txt in cnt.keys():
                    cnt[txt] += 1
                else:
                    cnt[txt] = 1

        for k, v in cnt.items():
            if max(cnt.values()) > 1 and cnt[k] == max(cnt.values()):
                answer.append(k)
    answer = sorted(answer)

    return answer