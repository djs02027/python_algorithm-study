arr = [1, 2, 3]
N = len(arr)
perm = [0] * N
used = [0] * N


def backtracking(k):
    if k == N:
        print(perm)
        return
    else:
        for i in range(N):
            if used[i]:
                continue
            perm[k] = arr[i]
            used[i] = 1
            backtracking(k + 1)
            used[i] = 0


backtracking(0)
