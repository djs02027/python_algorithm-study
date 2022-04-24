T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    step = 0
    for i in range(1, K + 1):
        flag=False
        step = step + M
        if step > len(numbers):
            tmp = step - len(numbers)
            step = tmp
        elif step==len(numbers):
            tmp = step - len(numbers)
            flag=True
        if flag==False:
            cnt = numbers[step - 1] + numbers[step]
            numbers[step:step] = [cnt]
        else:
            cnt = numbers[step-1] + numbers[0]
            numbers.append(cnt)

    print('#{} {}'.format(tc, ' '.join(map(str,numbers[-10::][::-1]))))
