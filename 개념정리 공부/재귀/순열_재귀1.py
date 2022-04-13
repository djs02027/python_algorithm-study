# 재귀의 원리 -> 재귀로 구현한다면..
arr = [1, 2, 3]
N = len(arr)
perm = []


def backtracking(k): #0 #1 #2 #3 #2 #1 #2 #3
    if k == N:
        print(perm) #123
        return
    else:
        for i in arr: #1 #12 #123 #3 #3 #2 #3 #1 #2
            if i in perm:
                continue
            perm.append(i) #1 -#2 -#3
            backtracking(k+1)
            perm.pop() #12X #1XX #13 #132

backtracking(0)