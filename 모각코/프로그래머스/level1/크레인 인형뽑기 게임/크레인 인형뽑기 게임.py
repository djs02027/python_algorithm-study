def solution(board, moves):
    cnt = 0
    basket = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1]:
                basket.append(board[i][m - 1])
                board[i][m - 1] = 0
                break;

        for j in range(0, len(basket) - 1):
            if basket[j] == basket[j + 1]:
                basket[j] = 0;
                basket[j + 1] = 0
                cnt += 2
        tmp = []
        for k in range(len(basket)):
            if basket[k]:
                tmp.append(basket[k])
        basket = list(tmp)

    answer = cnt
    return answer