def solution(price, money, count):
    cac=0
    for i in range (1,count+1):
        cac+= price*i
    if money-cac<0:
        answer=abs(money-cac)
    else:
        answer=0

    return answer