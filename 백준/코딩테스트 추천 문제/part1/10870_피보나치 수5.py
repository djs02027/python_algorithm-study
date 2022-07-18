N=int(input())
answer=[0,1]
while len(answer)<=N:
    answer.append(sum(answer[-2:]))
print(answer[N])

