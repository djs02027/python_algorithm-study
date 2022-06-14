def solution(name):
    SP=65 #A_index
    EP=91 #Z_index+1
    total=0
    min_move = len(name) - 1
    for i, n in enumerate(name):
        S=(ord(n)-SP)
        E=(EP-ord(n))
        total=total+(min(S,E))
        next=i+1
        
        #현재 문자열을 기반으로 다음문자열에 연속된 A가 있는지 판별
        while next<len(name) and name[next]=="A":
            next+=1
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신    
        min_move = min(min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next))
       

    answer=total+ min_move
    return answer
