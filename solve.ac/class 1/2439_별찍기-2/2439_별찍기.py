num=int(input())
flag=num
for i in range(num):
    flag -= 1
    for j in range(num):
        if flag<=j:
            print('*', end="")
        else:
            print(' ', end="")
    print()
