def solution(lottos, win_nums):
    cac = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 0: 6}
    match_cnt = 0
    for wn in win_nums:
        if wn in lottos:
            match_cnt += 1
    total = match_cnt + lottos.count(0)
    answer = [cac.get(total), cac.get(match_cnt)]
    return answer
