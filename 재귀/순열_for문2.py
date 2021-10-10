#재귀의 원리 -> 재귀를 for문으로 구현한다면..
#방문표기하여 배열표시
arr=[1,2,3]
N=len(arr)
used=[0]*N
perm=[0]*N
for i in range(N):
    if used[i]:
        continue
    perm[0]=arr[i]
    used[i]=1
    #=========================================
    for j in range(N):
        if used[j]:
            continue
        perm[1] = arr[j]
        used[j] = 1
        # =========================================
        for k in range(N):
            if used[k]:
                continue
            perm[2] = arr[k]
            used[k] = 1
            # =========================================
            print(perm)
            # =========================================
            used[k] = 0
        # =========================================
        used[j] = 0
    # =========================================
    used[i] = 0