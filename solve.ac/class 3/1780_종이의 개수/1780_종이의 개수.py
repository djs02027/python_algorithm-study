def cutting(n, m, len_N):
    global cnt
    visited = [0, 0, 0]

    for i in range(0, n, len_N):
        for j in range(i, i + (len_N)):
            for k in range(m, m + (len_N)):
                visited[int(paper[j][k])] += 1
        # print(visited)
        flag = False
        for v in range(len(visited)):
            if visited[v] == (len_N*len_N):
                cnt[v] += 1
                flag = True
                break
        if flag == False:
            cnt[0] += visited[0]
            cnt[1] += visited[1]
            cnt[2] += visited[2]
        # print(cnt)
        visited = [0, 0, 0]
        # print("---")




N = int(input())
paper = [input().split() for _ in range(N)]
len_N = N
cnt = [0, 0, 0]
#####
breakflag=False
while True:

    # print(len_N)
    if N>3:
        len_N = len_N // 3
    if len_N == 1:
           break
    for i in range(0, N, len_N):
        cutting(N, i, len_N)
    if N<=3:
        len_N = len_N // 3

print(cnt[2])
print(cnt[0])
print(cnt[1])
