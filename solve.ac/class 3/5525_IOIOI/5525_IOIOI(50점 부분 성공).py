N = int(input())
M = int(input())
txt = input()
I = N + 1
O = N
Total = I + O
compare = ''
for i in range(Total):
    if i % 2 == 0:
        compare += 'I'
    else:

        compare += 'O'
cnt=0
for i in range(len(txt)):
    if txt[i:i + Total] ==compare:
        cnt+=1
print(cnt)