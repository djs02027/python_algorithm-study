#재귀의 원리 -> 재귀를 for문으로 구현한다면..

arr=[1,2,3]
perm=[]
for first in arr:
    if first in perm:
        continue
    perm.append(first)
    #=========================================
    for second in arr:
        if second in perm:
            continue
        perm.append(second)
        # =========================================
        for third in arr:
            if third in perm:
                continue
            perm.append(third)
            # =========================================
            print(perm)
            # =========================================
            perm.pop()
        # =========================================
        perm.pop()
    # =========================================
    perm.pop()