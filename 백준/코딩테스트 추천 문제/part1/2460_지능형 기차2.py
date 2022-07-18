T = 10
now = 0
answer = []
for _ in range(T):
    out_train, in_train = map(int, input().split())
    now = now - out_train
    now = now + in_train
    answer.append(now)
print(max(answer))
