import sys
input=sys.stdin.readline
def cutting(n, m, len_N):
    global cac
    flag=False
    for i in range(0, n, len_N):
        first=True
        first_vlaue=None


        for j in range(i, i + (len_N)):
            dif_flag = False
            Timeout = False
            for k in range(m, m + (len_N)):
                # print(paper[j][k],j, k)
                if first==True:
                    first_vlaue=paper[j][k]
                    first=False
                else:
                    if paper[j][k]!=first_vlaue:
                        dif_flag=True
                        Timeout=True
                        break
            if Timeout==True:
                break
        if dif_flag==False:
            cac[int(first_vlaue)]+=1
        else:
            for j in range(i, i + (len_N)):
                for k in range(m, m + (len_N)):
                    cac[int(paper[j][k])]+=1

        print(cac)

N = int(input().rstrip())
paper = [input().rstrip().split() for _ in range(N)]
len_N = N
cac=[0,0,0]
while True:
    if len_N == 1:
        break
    len_N = len_N // 3
    for i in range(0, N, len_N):
        cutting(N, i, len_N)

for i in range(len(cac)-1,-1,-1):
    print(cac[i])