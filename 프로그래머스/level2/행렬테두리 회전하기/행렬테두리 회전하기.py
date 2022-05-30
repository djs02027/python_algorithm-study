def solution(rows, columns, queries):
    answer = []
    x=1
    arrList=[]
    for i in range(rows):
        arrList.append([])
        for j in range(columns):
            arrList[i].append(x)
            x=x+1

    for s_c,s_r,e_c,e_r in queries:
        sc=s_c-1
        sr=s_r-1
        ec=e_c-1
        er=e_r-1
        Tmp=arrList[sc][sr]
        minv=Tmp
        try:
            for i in range(sc+1, ec+1):
                    minv=min(minv, arrList[i][sr])
                    arrList[i-1][sr]=arrList[i][sr]
            for i in range(sr+1,er+1):
                    minv=min(minv, arrList[ec][i])
                    arrList[ec][i-1]=arrList[ec][i]
            for i in range(ec-1,sc-1,-1):
                    minv=min(minv, arrList[i][er])
                    arrList[i+1][er]=arrList[i][er]
            for i in range(er-1,sr-1,-1):
                    minv=min(minv, arrList[sc][i])
                    arrList[sc][i+1]=arrList[sc][i]
            arrList[sc][sr+1]=Tmp
            answer.append(minv)
        except IndexError:
            print(i)
    return answer