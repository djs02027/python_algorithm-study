from itertools import combinations
def solution(orders, course):
    courseMenu=[]
    courseorder=set()
    for o in orders:
        order=[]
        for i in range(len(o)):
            order.append(o[i])
        orderlen=len(order)
        totalcombi=[]
        for i in range(2, orderlen+1):
            totalcombi=(list(combinations(order,i)))
            for t in totalcombi:
                t=list(t)
                t.sort()
                courseone=''.join(map(str,t))
                courseMenu.append(courseone)
                courseorder.add(courseone)
    result=[]
    for c in courseorder:
        num=courseMenu.count(c)
        result.append([c,num])
    result.sort(key=lambda x: x[1])
    # print(courseMenu)
    # print(courseorder)
    print(result)
    answer = []
    return answer