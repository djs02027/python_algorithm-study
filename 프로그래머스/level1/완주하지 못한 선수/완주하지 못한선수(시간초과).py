def solution(participant, completion):
    for com in completion:
        participant.pop(participant.index(com))

    answer = ''.join(participant)
    return answer