from itertools import combinations
def solution(d, budget):
    N=len(d)
    total=[]
    maxv=1
    i=1
    d.sort()
    while True:
        if i==N+1:
            break
        total=list(combinations(d,i))
        cac=0
        for j in range(len(total)):
            cac=sum(total[j])
            if cac==budget:
                if maxv<len(total[j]):
                    maxv=len(total[j])
        i+=1
    print(maxv)
    answer = maxv
    return answer