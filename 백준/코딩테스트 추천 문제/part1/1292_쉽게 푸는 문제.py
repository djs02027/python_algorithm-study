start, end= map(int,input().split())
answer=[0]
N=1
while len(answer)<=1000:
    for i in range(N):
        answer.append(N)
    N=N+1

print(sum(answer[start:end+1]))
