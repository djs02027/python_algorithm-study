T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    txt = list(map(int, input().split()))
    Pizzas = []
    for i in range(len(txt)):
        Pizzas.append([i+1, txt[i]])

    InOven = Pizzas[:N]
    OutOven = Pizzas[N:]
    # print(InOven)
    # print(OutOven)
    while len(InOven) != 1:
        tmp = InOven.pop(0)
        num, Now = tmp[0],tmp[1]
        pizza = Now // 2
        if pizza > 0:
            InOven.append([num,pizza])
        else:
            if OutOven:
                InOven.append(OutOven.pop(0))
    print('#{} {}'.format(tc,InOven[0][0]))